import json
import os
import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Usage: python notify_slack.py <session.json>")
        sys.exit(1)

    json_path = sys.argv[1]

    # Load session info from the JSON file
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Failed to read JSON file: {e}")
        sys.exit(1)

    session = data.get("session_info", {})

    # Get environment variables
    system = os.getenv("FIRECREST_SYSTEM", "Unknown System")
    slack_url = os.getenv("SLACK_WEBHOOK_URL")
    pipeline_name = os.getenv("CI_PROJECT_PATH", "Unknown Pipeline")
    pipeline_url = os.getenv("CI_PIPELINE_URL", "#")
    test_report_url = f"{pipeline_url}/test_report"

    if not slack_url:
        print("❌ Missing SLACK_WEBHOOK_URL environment variable")
        sys.exit(1)

    # Compose Slack message
    if session.get("num_failures", 0) > 0 or session.get("num_aborted", 0) > 0:
        result_emoji = "❌"
    else:
        result_emoji = "✅"

    message = (
        f"*Test Report Notification*\n"
        f"> 🤖 *System:* {system}\n"
        f"> 🧱 *Pipeline:* <{pipeline_url}|{pipeline_name}>\n"
        f"> 📄 *Test Report:* <{test_report_url}|View Report>\n"
        f"> {result_emoji} *Tests:* {session.get('num_cases', 0)} total | "
        f"{session.get('num_failures', 0)} failed | "
        f"{session.get('num_aborted', 0)} aborted | "
        f"{session.get('num_skipped', 0)} skipped\n"
        f"> ⏱️ *Elapsed Time:* {round(session.get('time_elapsed', 0), 2)}s"
    )


    # Send message to Slack
    try:
        response = requests.post(
            slack_url,
            json={"text": message},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code != 200:
            print("❌ Failed to send Slack message:", response.text)
        else:
            print("✅ Slack notification sent successfully!")
    except Exception as e:
        print(f"❌ Error sending message to Slack: {e}")

if __name__ == "__main__":
    main()
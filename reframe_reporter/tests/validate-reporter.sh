#!/bin/bash

source /Users/perettig/cscs/testing/reframe/.venv/bin/activate
export SCRATCH=aa

# daint production
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--system daint --mode production \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/tests/snapshots/uenv-inventory/uenv_image_inventory_daint.json \
-o cscs-reframe-tests/reframe_reporter/tests/snapshots/
# daint maintenance
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--system daint --mode maintenance \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/tests/snapshots/uenv-inventory/uenv_image_inventory_daint.json \
-o cscs-reframe-tests/reframe_reporter/tests/snapshots

# Matrix production
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--matrix-mode daint-prod:daint:production,eiger-prod:eiger:production,santis-prod:santis:production,clariden-prod:clariden:production \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/tests/snapshots/uenv-inventory/uenv_image_inventory_daint_eiger_santis_clariden.json \
-o cscs-reframe-tests/reframe_reporter/tests/snapshots \
-f eligible_tests_matrix_mode-production.md

# Matrix maintenance
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--matrix-mode daint-maint:daint:maintenance,eiger-maint:eiger:maintenance,santis-maint:santis:maintenance,clariden-maint:clariden:maintenance \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/tests/snapshots/uenv-inventory/uenv_image_inventory_daint_eiger_santis_clariden.json \
-o cscs-reframe-tests/reframe_reporter/tests/snapshots \
-f eligible_tests_matrix_mode-maintenance.md



import json
import os
import pathlib
import yaml

import reframe.utility.osext as osext
from reframe.core.exceptions import ConfigError
from packaging.version import Version


_UENV_MOUNT_DEFAULT = '/user-environment'
_UENV_CLI = 'uenv'
_UENV_DELIMITER = ','
_UENV_MOUNT_DELIMITER = '@'
_RFM_META = pathlib.Path('extra') / 'reframe.yaml'
_RFM_META_DIR = pathlib.Path('meta')
UENV_RECIPES_ENVVAR = 'RFM_UENV_RECIPES_DIR'


def uarch(partition):
    """
    Return the uenv uarch tag of the nodes in a reframe partition description.

    partition: reframe partition information
    returns:
       'a100', 'gh200', 'mi200', 'mi300', 'zen2' or 'zen3'
       None -> unable to identify uarch
    """
    gpus = partition.devices
    if gpus:
        device = gpus[0]
        if device.arch == 'sm_90':
            return 'gh200'
        if device.arch == 'sm_80':
            return 'a100'
        if device.arch == 'gfx90a':
            return 'mi200'
        if device.arch == 'gfx942':
            return 'mi300'
        return None

    cpus = partition.processor
    if cpus.arch == 'zen2':
        return 'zen2'
    if cpus.arch == 'zen3':
        return 'zen3'

    return None


def uenv_metadata():
    # import os
    # import json
    # from reframe.utility import osext

    uenv_label = os.environ['UENV']
    _uenv_version = osext.run_command(f'{_UENV_CLI} --version').stdout.strip()

    if Version(_uenv_version) >= Version('9.2.0'):
        _cmd = f"{_UENV_CLI} image inspect --json {uenv_label}"
        metadata = json.loads(osext.run_command(_cmd, shell=True).stdout)
        return Version(metadata["version"]), Version(metadata["tag"])
    else:
        _cmd = f"{_UENV_CLI} image inspect --format=\'{{version}} {{tag}}\' {uenv_label}"  # noqa E501
        _version_tag = osext.run_command(_cmd, shell=True).stdout
        return str(_version_tag.split(" ")[0]), \
            str(_version_tag.split(" ")[1])

def _load_uenv_recipes_deploy_map(recipe_dir_path: pathlib.Path) -> dict[str, list[str]]:
    config_path = recipe_dir_path.parent / 'config.yaml'
    if not config_path.is_file():
        raise ConfigError(
            f"Could not find config.yaml in {recipe_dir_path.parent}"
        )

    try:
        with open(config_path) as cfg:
            cfg_data = yaml.safe_load(cfg)
    except OSError as err:
        raise ConfigError(
            f"Cannot read {config_path}: {err}"
        )
    except yaml.YAMLError as err:
        raise ConfigError(
            f"Cannot parse {config_path}: {err}"
        )

    if not isinstance(cfg_data, dict):
        return {}

    uenvs = cfg_data.get('uenvs', {})
    if not isinstance(uenvs, dict):
        return {}

    recipe_to_systems: dict[str, list[str]] = {}
    for product, versions in uenvs.items():
        if not isinstance(versions, dict):
            continue

        for version, desc in versions.items():
            if not isinstance(desc, dict):
                continue

            recipes = desc.get('recipes', {})
            deploy = desc.get('deploy', {})
            if not isinstance(recipes, dict) or not isinstance(deploy, dict):
                continue

            for system, variants in deploy.items():
                variant_list = []
                if isinstance(variants, list):
                    variant_list = variants
                elif isinstance(variants, str):
                    variant_list = [variants]
                else:
                    continue

                for variant in variant_list:
                    recipe_subpath = recipes.get(variant)
                    if not recipe_subpath:
                        continue

                    full_path = pathlib.Path(product) / str(recipe_subpath)
                    key = full_path.as_posix()
                    recipe_to_systems.setdefault(key, []).append(system)

    return recipe_to_systems


def _load_uenvs_from_recipes(recipe_dir: str) -> list[dict]:
    recipe_dir_path = pathlib.Path(recipe_dir).expanduser().resolve()
    if not recipe_dir_path.is_dir():
        raise ConfigError(
            f"{UENV_RECIPES_ENVVAR} path is not a directory: "
            f"{recipe_dir}"
        )

    recipe_deploy_map = _load_uenv_recipes_deploy_map(recipe_dir_path)
    uenv_environments = []
    for rfm_meta in recipe_dir_path.rglob('extra/reframe.yaml'):
        recipe_root = rfm_meta.parent.parent
        uenv_name = recipe_root.relative_to(recipe_dir_path).as_posix()
        uenv_name_pretty = uenv_name.replace('/', '_').replace(':', '_')

        try:
            with open(rfm_meta) as image_envs:
                image_environments = yaml.load(
                    image_envs.read(), Loader=yaml.BaseLoader)
        except OSError as err:
            print(
                f'Skipping local uenv recipe `{rfm_meta}`, there was an error '
                f'reading the metadata: {err}'
            )
            continue

        if not isinstance(image_environments, dict):
            continue

        recipe_root = rfm_meta.parent.parent
        relative_recipe_path = recipe_root.relative_to(recipe_dir_path).as_posix()
        target_systems = recipe_deploy_map.get(relative_recipe_path, [])
        if not target_systems:
            continue

        for k, v in image_environments.items():
            if not isinstance(v, dict):
                continue

            env = {'target_systems': target_systems}
            env.update(v)

            activation = env.pop('activation', [])
            views = env.pop('views', [])

            if isinstance(activation, list):
                env['prepare_cmds'] = activation
            elif isinstance(activation, str):
                env['prepare_cmds'] = [f'source {activation}']
            else:
                raise ConfigError(
                    'activation has to be a list of commands to be '
                    'executed to configure the environment'
                )

            features = env.get('features', [])
            if isinstance(features, str):
                features = [features]
            env['features'] = list(features) + ['uenv']

            env['name'] = f'{uenv_name_pretty}_{k}'
            env['resources'] = {
                'uenv': {
                    'file': str(recipe_root),
                    'mount': None,
                    'uenv': str(recipe_root),
                }
            }
            if views:
                env['resources']['uenv_views'] = {
                    'views': ','.join(views)
                }

            uenv_environments.append(env)

    return uenv_environments

def _get_uenvs():
    recipes_dir = os.environ.get(UENV_RECIPES_ENVVAR, None)
    if recipes_dir:
        return _load_uenvs_from_recipes(recipes_dir)

    uenv = os.environ.get('UENV', None)
    if uenv is None:
        return uenv

    uenv_environments = []
    uenv_list = uenv.split(_UENV_DELIMITER)
    uenv_version = osext.run_command(
        f'{_UENV_CLI} --version', shell=True
    ).stdout.strip()

    for uenv in uenv_list:
        uenv_name, *image_mount = uenv.split(_UENV_MOUNT_DELIMITER)
        if len(image_mount) > 0:
            image_mount = image_mount[0]
        else:
            image_mount = None

        # Check if given uenv_name is a path to a squashfs archive
        uenv_path = pathlib.Path(uenv_name)
        if uenv_path.is_file():
            # We cannot inspect for target systems
            target_system = '*'
            image_path = uenv_path
            rfm_meta = image_path.parent / _RFM_META_DIR / _RFM_META
        else:
            inspect_cmd = f'{_UENV_CLI} image inspect {uenv_name} --format'

            image_path = osext.run_command(
                f"{inspect_cmd}='{{sqfs}}'", shell=True).stdout.strip()
            target_system = osext.run_command(
                f"{inspect_cmd}='{{system}}'", shell=True).stdout.strip()

            image_path = pathlib.Path(image_path)
            # Check that uenv was pulled
            if not image_path.is_file():
                raise ConfigError(
                    f"{uenv_name} is missing, "
                    f"try pulling it with: uenv image pull {uenv_name}")
            try:
                if image_path.stat().st_size == 0:
                    raise ConfigError(
                        f"{uenv_name} is empty, "
                        f"try pulling it with: uenv image pull {uenv_name}")
            except FileNotFoundError:
                raise ConfigError(f"{uenv_name} was not found")

            # FIXME temporary workaround for older uenv versions
            if Version(uenv_version) >= Version('5.1.0-dev'):
                meta_path = osext.run_command(
                    f"{inspect_cmd}='{{meta}}'", shell=True
                ).stdout.strip()
                rfm_meta = pathlib.Path(meta_path) / _RFM_META
            else:
                rfm_meta = image_path.parent / 'store.yaml'

        try:
            with open(rfm_meta) as image_envs:
                image_environments = yaml.load(
                    image_envs.read(), Loader=yaml.BaseLoader)
        except OSError as err:
            print(f'Skipping uenv `{uenv}`, there was an error '
                  f'reading the metadata: {err}')

            continue

        for k, v in image_environments.items():
            # strip out the fields that are not to be part reframe environment
            activation = v.pop('activation', [])
            views = v.pop('views', [])

            env = {
                'target_systems': [target_system]
            }
            env.update(v)

            if isinstance(activation, list):
                env['prepare_cmds'] = activation
            # FIXME: this is deprecated and should be removed
            elif isinstance(activation, str):
                env['prepare_cmds'] = [f'source {activation}']
            else:
                raise ConfigError(
                    'activation has to be a list of commands to be '
                    'executed to configure the environment'
                )

            # Replace characters that create problems in environment names
            uenv_name_pretty = \
                uenv_name.replace(":", "_").replace("/", "_").replace("%", "_")
            env['name'] = f'{uenv_name_pretty}_{k}'
            env['resources'] = {
                'uenv': {
                    'file': str(image_path),
                    'mount': image_mount,
                    'uenv': f'{image_path}:{image_mount}' if image_mount
                            else str(image_path)
                }
            }
            if len(views) > 0:
                env['resources']['uenv_views'] = {'views': ','.join(views)}
            env['features'] += ['uenv']
            if env['name'].startswith('prgenv'):
                env['features'] += ['prgenv']

            uenv_environments.append(env)

    return uenv_environments


UENV = _get_uenvs() or None

## Eligible ReFrame Tests on daint

- Filters:
  - system: `daint`
  - tags: `vs-node-validator`
  - checks: `25`
- Generated: `2026-06-02 15:02:22 +0200`

| Test name | Description | Category |
|----------|-------------|----------|
| [uenv_status](../checks/system/uenv/uenv_status.py) | — | [system/uenv](../checks/system/uenv/) |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('capstor/scratch/cscs', 'lustre') | Test mount points in the system | [system/integration](../checks/system/integration/) |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('capstor/store/cscs', 'lustre') | Test mount points in the system | [system/integration](../checks/system/integration/) |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('iopsstor/scratch/cscs', 'lustre') | Test mount points in the system | [system/integration](../checks/system/integration/) |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('iopsstor/store/cscs', 'lustre') | Test mount points in the system | [system/integration](../checks/system/integration/) |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('/users', 'nfs') | Test mount points in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=netcat | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12-fortran | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=htop | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=lsof | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=libtool | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=ltrace | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=ansible | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=bubblewrap | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=nnn | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=wget | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=pycxi-utils | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=datacenter-gpu-manager | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12-c++ | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=lua-lmod | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12 | Test pkgs installation in the system | [system/integration](../checks/system/integration/) |
| [EnvVariableConfigTest](../checks/system/integration/v-cluster_config.py)<br>• %envs_info=('APPS', '/capstor/apps/cscs/daint') | Test environment variables of the system | [system/integration](../checks/system/integration/) |
| [EnvVariableConfigTest](../checks/system/integration/v-cluster_config.py)<br>• %envs_info=('SCRATCH', '/capstor/scratch/cscs/') | Test environment variables of the system | [system/integration](../checks/system/integration/) |
| [DcgmRpmCheck](../checks/system/gssr/dcgm_hook.py) | Check DCGM executable and libraries are installed | [system/gssr](../checks/system/gssr/) |
| [GssrCeHookCheck](../checks/system/gssr/dcgm_hook.py)<br>• %pytorch_image_tag=25.01-py3_nvrtc-12.9 | Check DCGM CE hook is working with gssr | [system/gssr](../checks/system/gssr/) |
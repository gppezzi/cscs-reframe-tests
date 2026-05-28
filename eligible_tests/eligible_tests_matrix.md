## Test Coverage Matrix

- Generated: `2026-05-28 18:36:57 +0200`

### apps/pytorch

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [MLperfStorageCECleanup](../checks/apps/pytorch/mlperf_storage_ce.py)<br>• %mlperf.mlperf_data.base_dir=/capstor/scratch/cscs/ | ✅ | ❌ | ✅ | ✅ |
| [MLperfStorageCECleanup](../checks/apps/pytorch/mlperf_storage_ce.py)<br>• %mlperf.mlperf_data.base_dir=/iopsstor/scratch/cscs/ | ✅ | ❌ | ✅ | ✅ |
| [PyTorchDdpCeNv](../checks/apps/pytorch/pytorch_nvidia.py)<br>• %num_nodes=1<br>• %aws_ofi_nccl=True<br>• %image=nvcr.io#nvidia/pytorch:25.06-py3 | ✅ | ❌ | ✅ | ✅ |
| [PyTorchDdpCeNvlarge](../checks/apps/pytorch/pytorch_nvidia.py)<br>• %num_nodes=3<br>• %aws_ofi_nccl=True<br>• %image=nvcr.io#nvidia/pytorch:25.06-py3 | ✅ | ❌ | ✅ | ✅ |
| [PyTorchDdpCeNvlarge](../checks/apps/pytorch/pytorch_nvidia.py)<br>• %num_nodes=8<br>• %aws_ofi_nccl=True<br>• %image=nvcr.io#nvidia/pytorch:25.06-py3 | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_CE](../checks/apps/pytorch/pytorch_megatronlm.py)<br>• %model=llama3-70b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_CE](../checks/apps/pytorch/pytorch_megatronlm.py)<br>• %model=llama3-8b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_CE_apertus70b](../checks/apps/pytorch/pytorch_megatronlm.py)<br>• %model=apertus3-70b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchNCCLAllReduce](../checks/apps/pytorch/pytorch_allreduce.py)<br>• %image=nvcr.io#nvidia/pytorch:25.06-py3 | ✅ | ❌ | ✅ | ✅ |
| [test_image_tag_retrieval](../checks/apps/pytorch/pytorch_nvidia.py) | ✅ | ❌ | ✅ | ✅ |

### containers/container_engine

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CUDA_MPS_CE](../checks/containers/container_engine/cuda_mps.py) | ✅ | ❌ | ✅ | ✅ |
| [OMB_MPICH_CE](../checks/containers/container_engine/omb.py)<br>• %test_name=collective/osu_alltoall | ✅ | ❌ | ✅ | ✅ |
| [OMB_MPICH_CE](../checks/containers/container_engine/omb.py)<br>• %test_name=pt2pt/osu_bw | ✅ | ❌ | ✅ | ✅ |
| [OMB_OMPI_CE](../checks/containers/container_engine/omb.py)<br>• %test_name=collective/osu_alltoall | ✅ | ❌ | ✅ | ✅ |
| [OMB_OMPI_CE](../checks/containers/container_engine/omb.py)<br>• %test_name=pt2pt/osu_bw | ✅ | ❌ | ✅ | ✅ |
| [PyFR_CE](../checks/containers/container_engine/pyfr.py)<br>• %backend=cuda<br>• %test_name=3d-taylor-green-ci | ✅ | ❌ | ✅ | ✅ |
| [PyFR_Skybox](../checks/containers/container_engine/pyfr.py)<br>• %backend=cuda<br>• %test_name=3d-taylor-green-ci | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_CE_Dev](../checks/containers/container_engine/pytorch_megatronlm.py)<br>• %model=llama3-8b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_Skybox](../checks/containers/container_engine/pytorch_megatronlm.py)<br>• %model=llama3-8b | ✅ | ❌ | ✅ | ✅ |
| [SSH_CE](../checks/containers/container_engine/ssh.py) | ✅ | ✅ | ✅ | ✅ |
| [SphExa_CE](../checks/containers/container_engine/sphexa.py)<br>• %sph_infile=/sphexa/50c.h5<br>• %num_gpus=8<br>• %sph_testcase=evrard<br>• %sph_steps=10<br>• %sph_size=200 | ✅ | ❌ | ✅ | ✅ |
| [SphExa_Skybox](../checks/containers/container_engine/sphexa.py)<br>• %sph_infile=/sphexa/50c.h5<br>• %num_gpus=8<br>• %sph_testcase=evrard<br>• %sph_steps=10<br>• %sph_size=200 | ✅ | ❌ | ✅ | ✅ |

### libraries/io

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CPE_HDF5Test](../checks/libraries/io/hdf5.py)<br>• %lang=cpp | ✅ | ✅ | ❌ | ❌ |
| [CPE_HDF5Test](../checks/libraries/io/hdf5.py)<br>• %lang=f90 | ✅ | ✅ | ❌ | ❌ |

### microbenchmarks/cpu/stream

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [StreamTest](../checks/microbenchmarks/cpu/stream/stream.py) | ✅ | ✅ | ❌ | ❌ |

### microbenchmarks/cpu_gpu/node_burn

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CPUNodeBurnGemmCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ✅ | ✅ | ✅ |
| [CPUNodeBurnStreamCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ✅ | ✅ | ✅ |
| [CudaNodeBurnGemmCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ❌ | ✅ | ✅ |
| [CudaNodeBurnStreamCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/gpu/node_burn

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [baremetal_cuda_node_burn](../checks/microbenchmarks/gpu/node_burn/baremetal-node-burn.py) | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/mpi/osu

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_allreduce<br>• %num_nodes=6<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ❌ | ❌ |
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_alltoall<br>• %num_nodes=6<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ❌ | ❌ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_bw<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ❌ | ❌ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_latency<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ❌ | ❌ |

### microbenchmarks/xccl

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [NCCLTestsCE](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=all_reduce<br>• %image_tag=cuda12.9.1-ubuntu24.04 | ✅ | ❌ | ✅ | ✅ |
| [NCCLTestsCE](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=sendrecv<br>• %image_tag=cuda12.9.1-ubuntu24.04 | ✅ | ❌ | ✅ | ✅ |

### prgenv

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [AlternateSocketFilling](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [ConsecutiveSocketFilling](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-R | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-hdf5 | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-hdf5-parallel | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-mpich | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=cudatoolkit | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckDaint](../checks/prgenv/environ_check.py)<br>• %cray_module=papi | ✅ | ❌ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-R | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-hdf5 | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-hdf5-parallel | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-mpich | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-openshmemx | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-parallel-netcdf | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=cray-pmi | ❌ | ✅ | ❌ | ❌ |
| [CrayVariablesCheckEiger](../checks/prgenv/environ_check.py)<br>• %cray_module=papi | ❌ | ✅ | ❌ | ❌ |
| [DefaultPrgEnvCheck](../checks/prgenv/environ_check.py) | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ❌ | ❌ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ❌ | ❌ |
| [MpiInitTest](../checks/prgenv/mpi.py) | ✅ | ✅ | ❌ | ❌ |
| [OneTaskPerNumaNode](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneTaskPerSocketOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneTaskPerSocketOpenMPnomt](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneThreadPerLogicalCoreOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneThreadPerPhysicalCoreOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneThreadPerPhysicalCoreOpenMPnomt](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [OneThreadPerSocketOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ❌ | ❌ |
| [cpi_build_test](../checks/prgenv/mpi_cpi.py) | ✅ | ✅ | ❌ | ❌ |

### system/ce

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [RunJobCE](../checks/system/ce/ce_import_run_image.py) | ✅ | ✅ | ✅ | ✅ |
| [RunNVGPUJobCE](../checks/system/ce/ce_import_run_image.py) | ✅ | ❌ | ✅ | ✅ |

### system/gssr

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [DcgmRpmCheck](../checks/system/gssr/dcgm_hook.py) | ✅ | ❌ | ✅ | ✅ |
| [GssrCeHookCheck](../checks/system/gssr/dcgm_hook.py)<br>• %pytorch_image_tag=25.01-py3_nvrtc-12.9 | ✅ | ❌ | ✅ | ✅ |

### system/integration

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [EnvVariableConfigTest](../checks/system/integration/v-cluster_config.py)<br>• %envs_info=('APPS', '/capstor/apps/cscs/daint') | ✅ | ✅ | ✅ | ✅ |
| [EnvVariableConfigTest](../checks/system/integration/v-cluster_config.py)<br>• %envs_info=('SCRATCH', '/capstor/scratch/cscs/') | ✅ | ✅ | ✅ | ✅ |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('/users', 'nfs') | ✅ | ✅ | ✅ | ✅ |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('capstor/scratch/cscs', 'lustre') | ✅ | ✅ | ✅ | ✅ |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('capstor/store/cscs', 'lustre') | ✅ | ✅ | ✅ | ✅ |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('iopsstor/scratch/cscs', 'lustre') | ✅ | ✅ | ✅ | ✅ |
| [MountPointExistsTest](../checks/system/integration/v-cluster_config.py)<br>• %mount_info=('iopsstor/store/cscs', 'lustre') | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=ansible | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=bubblewrap | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=datacenter-gpu-manager | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12 | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12-c++ | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=gcc12-fortran | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=htop | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=libtool | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=lsof | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=ltrace | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=lua-lmod | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=netcat | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=nnn | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=pycxi-utils | ✅ | ✅ | ✅ | ✅ |
| [PackagePresentTest](../checks/system/integration/v-cluster_config.py)<br>• %tools_info=wget | ✅ | ✅ | ✅ | ✅ |
| [apps-path-check-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [curl-external-access](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [df-command-timeout](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [dns-external-host](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [dns-internal-host](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [dns-invalid-hostname](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [env-apps-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [env-home](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [env-project](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [env-scratch](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [env-store](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [env-tmp-not-set](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [fs-no-full](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [home-path-check](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [http-port-not-listening](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [ldap-getent-hosts](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [ldap-server-reachable](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [locale-check](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [mount-amd-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [mount-cray-pe-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [mount-intel-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [mount-scratch-capstor](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ❌ |
| [mount-scratch-iopsstor](../checks/system/integration/alps.py) | ❌ | ❌ | ❌ | ✅ |
| [mount-store-capstor](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [mount-users-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [netiface-hsn0-ip](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [netiface-hsn0-up](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [netiface-hsn1-ip](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-hsn1-up](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-hsn2-ip](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-hsn2-up](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-hsn3-ip](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-hsn3-up](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [netiface-nmn0-ip](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [netiface-nmn0-up](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [os-version-check-daint](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [os-version-check-eiger](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [ping-localhost](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [ping-remote-dns](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [ping-remote-http](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [project-path-check](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [scratch-path-check-capstor](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ❌ |
| [scratch-path-check-iopsstor](../checks/system/integration/alps.py) | ❌ | ❌ | ❌ | ✅ |
| [slurm-config-exists](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [slurm-munge-daemon](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [slurm-sinfo-tool](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [slurm-slurmctld-ping](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [ssh-port-listening](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [sshd-running](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [store-path-check](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [timeout-completes](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [timeout-signal-term](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [tool-emacs](../checks/system/integration/alps.py) | ❌ | ✅ | ❌ | ❌ |
| [tool-gcc](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [tool-gcc-12](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [tool-jq](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [tool-vim](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [tool-zypper](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [vsbase-nomad](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |
| [vservices-image-cp2k](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ❌ |
| [vservices-image-editors](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-gromacs](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ❌ |
| [vservices-image-icon-wcp-not-available](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ✅ |
| [vservices-image-lammps](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ❌ |
| [vservices-image-linaro-forge](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-namd](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ❌ |
| [vservices-image-netcdf-tools](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-prgenv-gnu](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-prgenv-nvidia-not-available](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-pytorch](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ✅ |
| [vservices-image-quantumespresso](../checks/system/integration/alps.py) | ✅ | ❌ | ✅ | ❌ |
| [vservices-image-vasp](../checks/system/integration/alps.py) | ✅ | ❌ | ❌ | ❌ |
| [vservices-uenv-version](../checks/system/integration/alps.py) | ✅ | ✅ | ✅ | ✅ |

### system/io

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ddBlockSizeTest](../checks/system/io/dd_blk_size.py) | ✅ | ✅ | ✅ | ✅ |
| [fio_compile_test](../checks/system/io/fio.py) | ❌ | ✅ | ❌ | ❌ |
| [stuck_gpu_mem_test](../checks/system/io/fio.py) | ✅ | ❌ | ✅ | ✅ |

### system/network

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CXIGPULoopbackBW](../checks/system/network/cxi_gpu_loopback_bw.py) | ✅ | ❌ | ✅ | ✅ |
| [CXIStatHSN](../checks/system/network/cxi_stat_hsn.py) | ✅ | ❌ | ✅ | ✅ |

### system/slurm

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [InvalidAccount](../checks/system/slurm/invalid_acc.py) | ✅ | ✅ | ✅ | ✅ |

### system/uenv

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [uenv_status](../checks/system/uenv/uenv_status.py) | ✅ | ✅ | ✅ | ✅ |


### Summary

| Metric | daint-maint | eiger-maint | santis-maint | clariden-maint |
|--------|--------|--------|--------|--------|
| TOTAL | 161 | 120 | 118 | 118 |
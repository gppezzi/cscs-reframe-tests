## Test Coverage Matrix

- Generated: `2026-06-03 10:07:44 +0200`

### apps/ascent

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [uenv_ascent_cloverleaf3d](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_doublegyre_cpp](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_doublegyre_python](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_heatdiffusion_cpp](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_heatdiffusion_python](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_binning_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_extract_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_extract_example2 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_extract_example3 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_extract_example4 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_first_light_example | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_pipeline_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_query_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_scene_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_scene_example2 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_scene_example3 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_scene_example4 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_intro_cpp](../checks/apps/ascent/ascent.py)<br>• %exe=ascent_trigger_example1 | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_kripke](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |
| [uenv_ascent_noise](../checks/apps/ascent/ascent.py) | ✅ | ❌ | ❌ | ❌ |

### apps/cp2k

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [Cp2kBuildTestUENV](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [Cp2kCheckMD_UENVCustomExec](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [Cp2kCheckMD_UENVExec](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [Cp2kCheckPBE_UENVCustomExec](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [Cp2kCheckPBE_UENVExec](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [Cp2kCheckRPA_UENVExec](../checks/apps/cp2k/cp2k_uenv.py) | ✅ | ❌ | ❌ | ❌ |

### apps/dummysph

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=binning | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=rendering | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=thresholding | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=binning | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=compositing | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=rendering | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=OFF<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=thresholding | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=binning | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=histsampling | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=rendering | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=OFF<br>• %test=thresholding | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=binning | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=compositing | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=histsampling | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=rendering | ✅ | ❌ | ❌ | ❌ |
| [dummysph_uenv_ascent_single](../checks/apps/dummysph/dummysph.py)<br>• %aos=OFF<br>• %fp64=ON<br>• %tipsy=OFF<br>• %h5part=ON<br>• %test=thresholding | ✅ | ❌ | ❌ | ❌ |

### apps/icon4py

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ICON4PyBenchmarks](../checks/apps/icon4py/icon4py_check.py) | ✅ | ❌ | ✅ | ✅ |

### apps/lammps

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [lammps_build_test](../checks/apps/lammps/lammps.py) | ✅ | ❌ | ❌ | ❌ |
| [lammps_gpu_test](../checks/apps/lammps/lammps.py) | ✅ | ❌ | ❌ | ❌ |
| [lammps_kokkos_test](../checks/apps/lammps/lammps.py) | ✅ | ❌ | ❌ | ❌ |

### apps/namd

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [NamdBuildTestUENV](../checks/apps/namd/namd_check_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [NamdCheckUENVCustomExec](../checks/apps/namd/namd_check_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [NamdCheckUENVExec](../checks/apps/namd/namd_check_uenv.py) | ✅ | ❌ | ❌ | ❌ |

### apps/paraview

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ParaView_catalystClipping](../checks/apps/paraview/paraview.py) | ✅ | ✅ | ✅ | ✅ |
| [ParaView_coloredSphere](../checks/apps/paraview/paraview.py) | ✅ | ✅ | ✅ | ✅ |

### apps/paraview/build-gadget-plugin

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ParaviewBuildGadgetPlugin](../checks/apps/paraview/build-gadget-plugin/paraview_buildgadgetplugin.py) | ✅ | ✅ | ✅ | ❌ |

### apps/paraview/catalystclipping

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ParaviewCatalystClipping](../checks/apps/paraview/catalystclipping/paraview_catalystclipping.py) | ✅ | ✅ | ✅ | ❌ |

### apps/paraview/coloredsphere

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [ParaviewColoredSphere](../checks/apps/paraview/coloredsphere/paraview_coloredsphere.py) | ✅ | ✅ | ✅ | ❌ |

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
| [PyTorchMegatronLM_UENV](../checks/apps/pytorch/pytorch_megatronlm.py)<br>• %model=llama3-70b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchMegatronLM_UENV](../checks/apps/pytorch/pytorch_megatronlm.py)<br>• %model=llama3-8b | ✅ | ❌ | ✅ | ✅ |
| [PyTorchNCCLAllReduce](../checks/apps/pytorch/pytorch_allreduce.py)<br>• %image=nvcr.io#nvidia/pytorch:25.06-py3 | ✅ | ❌ | ✅ | ✅ |
| [test_image_tag_retrieval](../checks/apps/pytorch/pytorch_nvidia.py) | ✅ | ❌ | ✅ | ✅ |

### apps/q-e-sirius

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [QeSiriusCheckAuSurfUENVExec](../checks/apps/q-e-sirius/q-e-sirius_check_uenv.py) | ✅ | ❌ | ❌ | ❌ |

### apps/quantumespresso

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [QeBuildTestUENV](../checks/apps/quantumespresso/quantumespresso_check_uenv.py) | ✅ | ❌ | ✅ | ❌ |
| [QeCheckAuSurfCustomExecUENV](../checks/apps/quantumespresso/quantumespresso_check_uenv.py) | ✅ | ❌ | ✅ | ❌ |
| [QeCheckAuSurfUENVExec](../checks/apps/quantumespresso/quantumespresso_check_uenv.py) | ✅ | ❌ | ✅ | ❌ |

### apps/sphexa

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [SphExa](../checks/apps/sphexa/sphexa_uenv.py)<br>• %sph_build_type=Release<br>• %sph_infile=50c.h5<br>• %num_gpus=4<br>• %sph_testcase=evrard<br>• %sph_steps=2<br>• %sph_side=150 | ✅ | ❌ | ✅ | ✅ |

### apps/vasp

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [VaspBuildCheckUENV](../checks/apps/vasp/vasp_check_uenv.py)<br>• %num_nodes=1 | ✅ | ❌ | ❌ | ❌ |
| [VaspBuildCheckUENV](../checks/apps/vasp/vasp_check_uenv.py)<br>• %num_nodes=2 | ✅ | ❌ | ❌ | ❌ |
| [VaspBuildTestUENV](../checks/apps/vasp/vasp_check_uenv.py) | ✅ | ❌ | ❌ | ❌ |
| [VaspCheckUENV](../checks/apps/vasp/vasp_check_uenv.py)<br>• %num_nodes=1 | ✅ | ❌ | ❌ | ❌ |
| [VaspCheckUENV](../checks/apps/vasp/vasp_check_uenv.py)<br>• %num_nodes=2 | ✅ | ❌ | ❌ | ❌ |

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

### libraries/dlaf

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [dlaf_check_uenv](../checks/libraries/dlaf/dlaf.py)<br>• %test_name=eigensolver | ✅ | ❌ | ❌ | ❌ |
| [dlaf_check_uenv](../checks/libraries/dlaf/dlaf.py)<br>• %test_name=gen_eigensolver | ✅ | ❌ | ❌ | ❌ |

### libraries/io

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [Uenv_HDF5Test](../checks/libraries/io/hdf5.py)<br>• %lang=cpp | ✅ | ✅ | ✅ | ✅ |
| [Uenv_HDF5Test](../checks/libraries/io/hdf5.py)<br>• %lang=f90 | ✅ | ✅ | ✅ | ✅ |

### microbenchmarks/cpu/stream

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [StreamTest](../checks/microbenchmarks/cpu/stream/stream.py) | ✅ | ✅ | ✅ | ✅ |

### microbenchmarks/cpu_gpu/node_burn

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CPUNodeBurnGemmCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ✅ | ✅ | ✅ |
| [CPUNodeBurnStreamCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ✅ | ✅ | ✅ |
| [CudaNodeBurnGemmCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ❌ | ✅ | ✅ |
| [CudaNodeBurnStreamCE](../checks/microbenchmarks/cpu_gpu/node_burn/node-burn-ce.py) | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/gpu/gpu_benchmarks

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [FFTBenchBuild](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py) | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=1D<br>• %fft_size=1024 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=1D<br>• %fft_size=128 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=1D<br>• %fft_size=256 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=1D<br>• %fft_size=512 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=2D<br>• %fft_size=1024 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=2D<br>• %fft_size=128 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=2D<br>• %fft_size=256 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=2D<br>• %fft_size=512 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=3D<br>• %fft_size=1024 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=3D<br>• %fft_size=128 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=3D<br>• %fft_size=256 | ✅ | ❌ | ✅ | ✅ |
| [FFTCheck](../checks/microbenchmarks/gpu/gpu_benchmarks/fft.py)<br>• %fft_dim=3D<br>• %fft_size=512 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=radix-sort<br>• %_executable_opts=21 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=radix-sort<br>• %_executable_opts=27 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=radix-sort<br>• %_executable_opts=30 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=reduce<br>• %_executable_opts=26 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=reduce<br>• %_executable_opts=29 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=reduce<br>• %_executable_opts=31 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=scan<br>• %_executable_opts=24 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=scan<br>• %_executable_opts=26 | ✅ | ❌ | ✅ | ✅ |
| [ParallelAlgos](../checks/microbenchmarks/gpu/gpu_benchmarks/parallel_algos.py)<br>• %algo=scan<br>• %_executable_opts=29 | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/gpu/gpu_burn

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [cscs_gpu_burn_check](../checks/microbenchmarks/gpu/gpu_burn/gpu_burn_test.py) | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/gpu/node_burn

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [baremetal_cuda_node_burn](../checks/microbenchmarks/gpu/node_burn/baremetal-node-burn.py) | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/mpi/osu

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [OSUBandwidth](../checks/microbenchmarks/mpi/osu/osu_run.py) | ✅ | ✅ | ✅ | ✅ |
| [OSUBandwidthCuda](../checks/microbenchmarks/mpi/osu/osu_run.py) | ✅ | ❌ | ✅ | ✅ |
| [OSULatency](../checks/microbenchmarks/mpi/osu/osu_run.py) | ✅ | ✅ | ✅ | ✅ |
| [OSULatencyCuda](../checks/microbenchmarks/mpi/osu/osu_run.py) | ✅ | ❌ | ✅ | ✅ |
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_allreduce<br>• %num_nodes=6<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ✅ | ✅ |
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_allreduce<br>• %num_nodes=6<br>• %osu_binaries.build_type=cuda | ✅ | ❌ | ✅ | ✅ |
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_alltoall<br>• %num_nodes=6<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ✅ | ✅ |
| [osu_collective_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.collective.blocking.osu_alltoall<br>• %num_nodes=6<br>• %osu_binaries.build_type=cuda | ✅ | ❌ | ✅ | ✅ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_bw<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ✅ | ✅ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_bw<br>• %osu_binaries.build_type=cuda | ✅ | ❌ | ✅ | ✅ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_latency<br>• %osu_binaries.build_type=cpu | ✅ | ✅ | ✅ | ✅ |
| [osu_pt2pt_check](../checks/microbenchmarks/mpi/osu/osu_tests.py)<br>• %benchmark_info=mpi.pt2pt.standard.osu_latency<br>• %osu_binaries.build_type=cuda | ✅ | ❌ | ✅ | ✅ |

### microbenchmarks/xccl

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [NCCLTestsCE](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=all_reduce<br>• %image_tag=cuda12.9.1-ubuntu24.04 | ✅ | ❌ | ✅ | ✅ |
| [NCCLTestsCE](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=sendrecv<br>• %image_tag=cuda12.9.1-ubuntu24.04 | ✅ | ❌ | ✅ | ✅ |
| [NCCLTestsUENV](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=all_reduce | ✅ | ❌ | ✅ | ✅ |
| [NCCLTestsUENV](../checks/microbenchmarks/xccl/xccl_tests.py)<br>• %test_name=sendrecv | ✅ | ❌ | ✅ | ✅ |

### prgenv

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [AlternateSocketFilling](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [ConsecutiveSocketFilling](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
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
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestMPI](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestMPIOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestOpenMP](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=F90 | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=c | ✅ | ✅ | ✅ | ✅ |
| [HelloWorldTestSerial](../checks/prgenv/helloworld.py)<br>• %linking=dynamic<br>• %lang=cpp | ✅ | ✅ | ✅ | ✅ |
| [MpiGpuDirectOOM](../checks/prgenv/mpi.py)<br>• %ipc=0 | ✅ | ❌ | ✅ | ✅ |
| [MpiGpuDirectOOM](../checks/prgenv/mpi.py)<br>• %ipc=1 | ✅ | ❌ | ✅ | ✅ |
| [MpiInitTest](../checks/prgenv/mpi.py) | ✅ | ✅ | ✅ | ✅ |
| [OneTaskPerNumaNode](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneTaskPerSocketOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneTaskPerSocketOpenMPnomt](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneThreadPerLogicalCoreOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneThreadPerPhysicalCoreOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneThreadPerPhysicalCoreOpenMPnomt](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [OneThreadPerSocketOpenMP](../checks/prgenv/affinity_check.py) | ✅ | ✅ | ✅ | ✅ |
| [UenvFixincludes](../checks/prgenv/uenv_fixincludes.py) | ✅ | ✅ | ✅ | ✅ |
| [cpi_build_test](../checks/prgenv/mpi_cpi.py) | ✅ | ✅ | ✅ | ✅ |

### prgenv/cuda

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [MPIIntranodePinned](../checks/prgenv/cuda/cuda_mpi_intranode_pinned.py)<br>• %mem=host<br>• %mpich_smp_single_copy_mode=CMA | ✅ | ❌ | ✅ | ✅ |
| [MPIIntranodePinned](../checks/prgenv/cuda/cuda_mpi_intranode_pinned.py)<br>• %mem=host<br>• %mpich_smp_single_copy_mode=XPMEM | ✅ | ❌ | ✅ | ✅ |
| [MPIIntranodePinned](../checks/prgenv/cuda/cuda_mpi_intranode_pinned.py)<br>• %mem=pinned_host<br>• %mpich_smp_single_copy_mode=CMA | ✅ | ❌ | ✅ | ✅ |
| [MPIIntranodePinned](../checks/prgenv/cuda/cuda_mpi_intranode_pinned.py)<br>• %mem=pinned_host<br>• %mpich_smp_single_copy_mode=XPMEM | ✅ | ❌ | ✅ | ✅ |
| [UENV_CudaSamples](../checks/prgenv/cuda/cuda_samples.py)<br>• %sample=conjugateGradient | ✅ | ❌ | ✅ | ✅ |
| [UENV_CudaSamples](../checks/prgenv/cuda/cuda_samples.py)<br>• %sample=deviceQuery | ✅ | ❌ | ✅ | ✅ |
| [UENV_CudaSamples](../checks/prgenv/cuda/cuda_samples.py)<br>• %sample=simpleCUBLAS | ✅ | ❌ | ✅ | ✅ |
| [UENV_NVML](../checks/prgenv/cuda/cuda_nvml.py) | ✅ | ❌ | ✅ | ✅ |
| [cuda_aware_mpi_build](../checks/prgenv/cuda/cuda_aware_mpi.py) | ✅ | ❌ | ✅ | ✅ |
| [cuda_aware_mpi_one_node_check](../checks/prgenv/cuda/cuda_aware_mpi.py) | ✅ | ❌ | ✅ | ✅ |
| [cuda_aware_mpi_two_nodes_check](../checks/prgenv/cuda/cuda_aware_mpi.py) | ✅ | ❌ | ✅ | ✅ |

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
| [fio_compile_test](../checks/system/io/fio.py) | ✅ | ✅ | ✅ | ✅ |
| [stuck_gpu_mem_test](../checks/system/io/fio.py) | ✅ | ❌ | ✅ | ✅ |

### system/network

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [CXIGPU2GPULoopbackBW](../checks/system/network/cxi_gpu_loopback_bw.py) | ✅ | ❌ | ✅ | ✅ |
| [CXIGPULoopbackBW](../checks/system/network/cxi_gpu_loopback_bw.py) | ✅ | ❌ | ✅ | ✅ |
| [CXIStatHSN](../checks/system/network/cxi_stat_hsn.py) | ✅ | ❌ | ✅ | ✅ |

### system/nvidia

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [UENV_NvidiaDeviceCount](../checks/system/nvidia/nvidia_device_count.py) | ✅ | ❌ | ✅ | ✅ |

### system/slurm

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [DefaultRequestGPUSetsGRES](../checks/system/slurm/slurm.py) | ✅ | ❌ | ✅ | ✅ |
| [EnvironmentVariableCheck](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [HostnameCheck](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [InvalidAccount](../checks/system/slurm/invalid_acc.py) | ✅ | ✅ | ✅ | ✅ |
| [MemoryOverconsumptionCheck](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [MemoryOverconsumptionCheckMPI](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [NVreg_RestrictProfilingToAdminUsers](../checks/system/slurm/slurm.py) | ✅ | ❌ | ✅ | ✅ |
| [NvidiaSmiDriverVersion](../checks/system/slurm/slurm.py) | ✅ | ❌ | ✅ | ✅ |
| [SlurmGPUGresTest](../checks/system/slurm/slurm.py) | ✅ | ❌ | ✅ | ✅ |
| [SlurmNoIsolCpus](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [SlurmParanoidCheck](../checks/system/slurm/slurm.py) | ✅ | ✅ | ✅ | ✅ |
| [SlurmQueueStatusCheck](../checks/system/slurm/slurm.py)<br>• %slurm_partition=debug | ✅ | ✅ | ✅ | ✅ |
| [SlurmQueueStatusCheck](../checks/system/slurm/slurm.py)<br>• %slurm_partition=low | ❌ | ✅ | ❌ | ❌ |
| [SlurmQueueStatusCheck](../checks/system/slurm/slurm.py)<br>• %slurm_partition=normal* | ✅ | ✅ | ✅ | ✅ |
| [SlurmQueueStatusCheck](../checks/system/slurm/slurm.py)<br>• %slurm_partition=prepost | ❌ | ✅ | ❌ | ❌ |
| [SlurmTransparentHugepagesCheck](../checks/system/slurm/slurm.py)<br>• %hugepages_options=always | ✅ | ❌ | ✅ | ✅ |
| [SlurmTransparentHugepagesCheck](../checks/system/slurm/slurm.py)<br>• %hugepages_options=default | ✅ | ❌ | ✅ | ✅ |
| [SlurmTransparentHugepagesCheck](../checks/system/slurm/slurm.py)<br>• %hugepages_options=madvise | ✅ | ❌ | ✅ | ✅ |
| [SlurmTransparentHugepagesCheck](../checks/system/slurm/slurm.py)<br>• %hugepages_options=never | ✅ | ❌ | ✅ | ✅ |
| [SlurmUvmPerfAccessCounterMigration](../checks/system/slurm/slurm.py) | ✅ | ❌ | ✅ | ✅ |
| [slurm_response_check](../checks/system/slurm/slurm.py)<br>• %command=sacct | ✅ | ✅ | ✅ | ✅ |
| [slurm_response_check](../checks/system/slurm/slurm.py)<br>• %command=squeue | ✅ | ✅ | ✅ | ✅ |

### system/uenv

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [uenv_status](../checks/system/uenv/uenv_status.py) | ✅ | ✅ | ✅ | ✅ |

### tools/profiling_and_debugging

| Test name | daint-maint | eiger-maint | santis-maint | clariden-maint |
|-----------|-----------|-----------|-----------|-----------|
| [linaro_ddt](../checks/tools/profiling_and_debugging/linaro_forge.py) | ✅ | ✅ | ✅ | ✅ |


### Summary

| Metric | daint-maint | eiger-maint | santis-maint | clariden-maint |
|--------|--------|--------|--------|--------|
| TOTAL | 277 | 119 | 208 | 202 |
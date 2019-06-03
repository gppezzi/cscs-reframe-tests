import os

import reframe as rfm
import reframe.utility.sanity as sn


class GridToolsCheckBase(rfm.RegressionTest):
    def __init__(self):
        super().__init__()
        self.descr = 'GridTools test base'

        self.valid_prog_environs = ['PrgEnv-gnu']
        self.modules = ['CMake/3.12.4', 'Boost', 'gcc/5.3.0']
        self.sourcesdir = 'https://github.com/GridTools/gridtools.git'
        self.build_system = 'CMake'

        self.sanity_patterns = sn.assert_found(r'PASSED', self.stdout)
        self.perf_patterns = {
            'wall_time': sn.extractsingle(r'(?P<timer>\w+) ms total',
                                     self.stdout, 'timer', int)
        }
        self.build_system.max_concurrency = 2
        self.tags = {'production'}
        self.maintainers = ['CB']

        self.variant_data = {
            'vertical_advection_dycore_naive': {
                'executable_opts':
                    ['150', '150', '150']
                ,
                'reference': {
                    'daint:mc': {
                        'wall_time': (3400, None, 0.1, 'ms')
                    },
                    'daint:gpu': {
                        'wall_time': (3800, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            },
            'vertical_advection_dycore_mc': {
                'executable_opts':
                    ['150', '150', '150']
                ,
                'reference': {
                    'daint:mc': {
                        'wall_time': (3500, None, 0.1, 'ms')
                    },
                    'daint:gpu': {
                        'wall_time': (3700, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            },
            'simple_hori_diff_naive': {
                'executable_opts':
                    ['100', '100', '100']
                ,
                'reference': {
                    'daint:mc': {
                        'wall_time': (3200, None, 0.1, 'ms')
                    },
                    'daint:gpu': {
                        'wall_time': (3700, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            },
            'simple_hori_diff_mc': {
                'executable_opts':
                    ['100', '100', '100']
                ,
                'reference': {
                    'daint:mc': {
                        'wall_time': (3300, None, 0.1, 'ms')
                    },
                    'daint:gpu': {
                        'wall_time': (3700, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            },
            'vertical_advection_dycore_cuda': {
                'executable_opts':
                    ['200', '200', '200']
                ,
                'reference': {
                    'daint:gpu': {
                        'wall_time': (10000, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            },
            'simple_hori_diff_cuda': {
                'executable_opts':
                    ['150', '150', '150']
                ,
                'reference': {
                    'daint:gpu': {
                        'wall_time': (13000, None, 0.1, 'ms')
                    },
                    '*': {
                        'wall_time': (0, None, None, 'ms')
                    }
                }
            }
        }

@rfm.parameterized_test(['vertical_advection_dycore_naive'], ['vertical_advection_dycore_mc'],
                        ['simple_hori_diff_naive'], ['simple_hori_diff_mc'])
class GridToolsCheckCPU(GridToolsCheckBase):
    def __init__(self, variant):
        super().__init__()
        self.descr = 'GridTools host test'

        self.build_system.config_opts = ['-DCMAKE_INSTALL_PREFIX=/scratch/snx3000/bignamic/reframe/cscs-checks/libraries/gridtools/install',
                                         '-DBoost_NO_BOOST_CMAKE="true"',
                                         '-DCMAKE_BUILD_TYPE:STRING=Release',
                                         '-DBUILD_SHARED_LIBS:BOOL=ON',
                                         '-DGT_ENABLE_TARGET_X86:BOOL=ON',
                                         '-DGT_ENABLE_TARGET_NAIVE:BOOL=ON',
                                         '-DGT_ENABLE_TARGET_CUDA:BOOL=OFF',
                                         '-DGT_ENABLE_TARGET_MC=ON',
                                         '-DGT_GCL_ONLY:BOOL=OFF',
                                         '-DCMAKE_CXX_COMPILER=CC',
                                         '-DGT_USE_MPI:BOOL=OFF',
                                         '-DGT_SINGLE_PRECISION:BOOL=OFF',
                                         '-DGT_ENABLE_PERFORMANCE_METERS:BOOL=ON',
                                         '-DGT_TESTS_ICOSAHEDRAL_GRID:BOOL=OFF',
                                         '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON',
                                         '-DBOOST_ROOT=$BOOST_ROOT',
                                         '-DGT_ENABLE_PYUTILS=OFF',
                                         '-DGT_TESTS_REQUIRE_FORTRAN_COMPILER=ON',
                                         '-DGT_TESTS_REQUIRE_C_COMPILER=ON',
                                         '-DCMAKE_EXPORT_NO_PACKAGE_REGISTRY=ON']


        self.valid_systems = ['daint:mc', 'daint:gpu']
        self.num_gpus_per_node = 0
        self.num_tasks = 1

        self.build_system.make_opts = [variant]
        self.executable = os.path.join('regression', variant)
        self.executable_opts = self.variant_data[variant]['executable_opts']
        self.reference = self.variant_data[variant]['reference']

@rfm.parameterized_test(['vertical_advection_dycore_cuda'], ['simple_hori_diff_cuda'])
class GridToolsCheckGPU(GridToolsCheckBase):
    def __init__(self, variant):
        super().__init__()
        self.descr = 'GridTools device test'

        self.modules.append('cudatoolkit/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8') TODO: uncomment

        self.build_system.config_opts = ['-DCMAKE_INSTALL_PREFIX=/scratch/snx3000/bignamic/reframe/cscs-checks/libraries/gridtools/install',
                                         '-DBoost_NO_BOOST_CMAKE="true"',
                                         '-DCMAKE_BUILD_TYPE:STRING=Release',
                                         '-DBUILD_SHARED_LIBS:BOOL=ON',
                                         '-DGT_ENABLE_TARGET_X86:BOOL=OFF',
                                         '-DGT_ENABLE_TARGET_NAIVE:BOOL=OFF',
                                         '-DGT_ENABLE_TARGET_CUDA:BOOL=ON',
                                         '-DCUDA_ARCH:STRING=sm_60',
                                         '-DGT_GCL_ONLY:BOOL=OFF',
                                         '-DCMAKE_CXX_COMPILER=CC',
                                         '-DCMAKE_CUDA_HOST_COMPILER:STRING=CC',
                                         '-DGT_USE_MPI:BOOL=OFF',
                                         '-DGT_SINGLE_PRECISION:BOOL=OFF',
                                         '-DGT_ENABLE_PERFORMANCE_METERS:BOOL=ON',
                                         '-DGT_TESTS_ICOSAHEDRAL_GRID:BOOL=OFF',
                                         '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON',
                                         '-DBOOST_ROOT=$BOOST_ROOT',
                                         '-DGT_ENABLE_PYUTILS=OFF',
                                         '-DGT_TESTS_REQUIRE_FORTRAN_COMPILER=ON',
                                         '-DGT_TESTS_REQUIRE_C_COMPILER=ON',
                                         '-DCMAKE_EXPORT_NO_PACKAGE_REGISTRY=ON']

        self.valid_systems = ['daint:gpu']
        self.num_gpus_per_node = 1
        self.num_tasks = 1

        self.build_system.make_opts = [variant]
        self.executable = os.path.join('regression', variant)
        self.executable_opts = self.variant_data[variant]['executable_opts']
        self.reference = self.variant_data[variant]['reference']

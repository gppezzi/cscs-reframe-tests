# Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn


class MemBandwidthTest(rfm.RunOnlyRegressionTest):
    modules = ['likwid']
    valid_prog_environs = ['PrgEnv-gnu']
    sourcesdir = None
    executable = 'likwid-bench'
    num_tasks = 1
    num_tasks_per_node = 1
    num_tasks_per_core = 2
    system_num_cpus = {
        'daint:mc':  72,
        'daint:gpu': 24,
        'dom:mc':  72,
        'dom:gpu': 24,
    }
    system_numa_domains = {
        'daint:mc':  ['S0', 'S1'],
        'daint:gpu': ['S0'],
        'dom:mc':  ['S0', 'S1'],
        'dom:gpu': ['S0'],
    }
    # Test each level at half capacity times nthreads per domain
    system_cache_sizes = {
        'daint:mc':  {'L1': '288kB', 'L2': '2304kB', 'L3': '23MB',
                      'memory': '1800MB'},
        'daint:gpu': {'L1': '192kB', 'L2': '1536kB', 'L3': '15MB',
                      'memory': '1200MB'},
        'dom:mc':    {'L1': '288kB', 'L2': '2304kB', 'L3': '23MB',
                      'memory': '1800MB'},
        'dom:gpu':   {'L1': '192kB', 'L2': '1536kB', 'L3': '15MB',
                      'memory': '1200MB'},
    }
    maintainers = ['SK', 'CB']
    tags = {'benchmark', 'diagnostic', 'health'}

    @sanity_function
    def assert_ge(self):
        self.bw_pattern = sn.min(sn.extractall(r'MByte/s:\s*(?P<bw>\S+)',
                                               self.stdout, 'bw', float))
        return sn.assert_ge(self.bw_pattern, 0.0)

    @performance_function('MB/s')
    def bandwidth(self):
        return self.bw_pattern


class CPUBandwidth(MemBandwidthTest):
    config = parameter([[[l, k] for l in ['L1', 'L2', 'L3']
                         for k in ['load_avx', 'store_avx']],
                        ['memory', 'load_avx'],
                        ['memory', 'store_mem_avx']])
    valid_systems = ['daint:mc', 'daint:gpu', 'dom:gpu', 'dom:mc']
    # the kernel to run in likwid
    kernel_name = variable(str)
    mem_level = variable(str)
    refs = {
        'mc':  {
            'load_avx': {'L1': 5100000, 'L2': 2000000, 'L3': 900000,
                         'memory': 130000},
            'store_avx': {'L1': 2800000, 'L2': 900000, 'L3': 480000},
            'store_mem_avx': {'memory': 85000},
        },
        'gpu': {
            'load_avx': {'L1': 2100000, 'L2': 850000, 'L3': 360000,
                         'memory': 65000},
            'store_avx': {'L1': 1200000, 'L2': 340000, 'L3': 210000},
            'store_mem_avx': {'memory': 42500},
        }
    }

    @run_after('init')
    def set_(self):
        self.mem_level, self.kernel_name = self.config
        self.descr = f'CPU <- {self.mem_level} {self.kernel_name} benchmark'
        ref_proxy = {part: refs[part][self.kernel_name][self.mem_level]
                     for part in refs.keys()}
        self.reference = {
            'daint:gpu': {
                'bandwidth': (ref_proxy['gpu'], -0.1, None, 'MB/s')
            },
            'daint:mc': {
                'bandwidth': (ref_proxy['mc'], -0.1, None, 'MB/s')
            },
            'dom:gpu': {
                'bandwidth': (ref_proxy['gpu'], -0.1, None, 'MB/s')
            },
            'dom:mc': {
                'bandwidth': (ref_proxy['mc'], -0.1, None, 'MB/s')
            },
        }

    @run_before('run')
    def set_exec_opts(self):
        partname = self.current_partition.fullname
        self.data_size = self.system_cache_sizes[partname][self.mem_level]
        self.num_cpus_per_task = self.system_num_cpus[partname]
        numa_domains = self.system_numa_domains[partname]
        num_cpu_domain = self.num_cpus_per_task // (len(numa_domains) *
                                                    self.num_tasks_per_core)
        # result for daint:mc: '-w S0:100MB:18:1:2 -w S1:100MB:18:1:2'
        # format: -w domain:data_size:nthreads:chunk_size:stride
        # chunk_size and stride affect which cpus from <domain> are selected
        workgroups = [f'-w {dom}:{self.data_size}:{num_cpu_domain:d}:1:2'
                      for dom in numa_domains]
        self.executable_opts = [f'-t {self.kernel_name}'] + workgroups


@rfm.simple_test
class CPUBandwidthCrossSocket(MemBandwidthTest):
    descr = ('CPU S0 <- main memory S1 read '
             'CPU S1 <- main memory S0 read')
    valid_systems = ['daint:mc', 'dom:mc']
    kernel_name = 'load_avx'
    reference = {
        'daint:mc': {
            'bandwidth': (56000, -0.1, None, 'MB/s')
        },
        'dom:mc': {
            'bandwidth': (56000, -0.1, None, 'MB/s')
        },
    }

    @run_before('run')
    def set_exec_opts(self):
        partname = self.current_partition.fullname
        self.num_cpus_per_task = self.system_num_cpus[partname]
        numa_domains = self.system_numa_domains[partname]

        num_cpu_domain = (self.num_cpus_per_task //
                          (len(numa_domains) * self.num_tasks_per_core))

        # daint:mc: '-w S0:100MB:18:1:2-0:S1 -w S1:100MB:18:1:2-0:S0'
        # format:
        # -w domain:data_size:nthreads:chunk_size:stride-stream_nr:mem_domain
        # chunk_size and stride affect which cpus from <domain> are selected
        workgroups = [f'-w {dom_cpu}:100MB:{num_cpu_domain:d}:1:2-0:{dom_mem}'
                      for dom_cpu, dom_mem in
                      zip(numa_domains[:2], reversed(numa_domains[:2]))]

        self.executable_opts = ['-t %s' % self.kernel_name] + workgroups

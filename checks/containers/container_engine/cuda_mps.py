# Copyright 2024 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import pathlib
import sys
import os

import reframe as rfm
import reframe.utility.sanity as sn

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent / 'mixins'))

from container_engine import ContainerEngineMixin  # noqa: E402


@rfm.simple_test
class CUDA_MPS_CE(rfm.RunOnlyRegressionTest, ContainerEngineMixin):
    valid_prog_environs = ['builtin']
    valid_systems = ['+ce +nvgpu']
    test_name = 'cuda_mps'
    num_nodes = variable(int, value=1)
    container_image = 'ubuntu:24.04'
    container_env_table = {
        'annotations.com.hooks': {
            'nvidia_cuda_mps.enabled': 'true',
        }
    }
    tags = {'production', 'ce'}

    executable = 'pgrep'
    executable_opts = ['--list-full', '--uid', f'{os.getuid()}', '--full', '"^nvidia-cuda-mps-control -d$"']

    @sanity_function
    def assert_sanity(self):
        return sn.assert_found(r'^\d+ nvidia-cuda-mps-control -d$', self.stdout)


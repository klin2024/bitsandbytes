# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from distutils.errors import DistutilsModuleError
from warnings import warn

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from setuptools.dist import Distribution


# Tested with wheel v0.29.0
class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True

setup(
    version="0.48.0",
    packages=find_packages(),
    distclass=BinaryDistribution,
    cmake_source_dir=".",
    package_data={
        "bitsandbytes" : ["libbitsandbytes_rocm.dll"]
    }
)

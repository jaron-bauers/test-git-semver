
# Copyright (c) 2022 Intel Corporation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pybuilder.core import use_plugin
from pybuilder.core import init
from pybuilder.core import Author

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_anybadge')

name = 'tgsver'
authors = [
    Author('Jaron Bauers', 'jaron.bauers@intel.com'),
    Author('Emilio Reyes', 'emilio.reyes@intel.com')]
summary = 'A Python script to execute git-semver functional tests'
url = 'https://github.com/jaron-bauers/test-git-semver'
version = '0.1.0'
default_task = [
    'clean',
    'analyze',
    'publish',
    'radon',
    'bandit',
    'anybadge']
license = 'Apache License, Version 2.0'
description = summary


@init
def set_properties(project):
    project.set_property('unittest_module_glob', 'test_*.py')
    project.set_property('coverage_break_build', False)
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_ignore', 'E501, W503, F401, F841')
    project.build_depends_on('mock')
    project.depends_on_requirements('requirements.txt')
    project.set_property('distutils_console_scripts', ['test-git-semver = tgsver.cli:main'])
    project.set_property('radon_break_build_average_complexity_threshold', 3.6)
    project.set_property('radon_break_build_complexity_threshold', 14)
    project.set_property('bandit_break_build', True)
    project.set_property('bandit_skip_ids', 'B404,B603,B604')
    project.set_property('anybadge_use_shields', True)
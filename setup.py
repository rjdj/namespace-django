##############################################################################
#
# Copyright (c) 2011 Reality Jockey Ltd. and Contributors.
# This file is part of namespace-django.
#
# Namespace-django is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Namespace-django is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with django-tornado. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import os
from setuptools import setup, find_packages

setup(name = "nsdjango",
      version = "0.1.1",
      author = 'Christian Haudum',
      author_email = 'christian.h@rjdj.me',
      description = 'Supports namespace packages as Django apps.',
      url = 'http://github.com/organizations/rjdj',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      install_requires = ['Django'],
      include_package_data = False,
      zip_safe = False,
)

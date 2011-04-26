import os
from setuptools import setup, find_packages

setup(name = "nsdjango",
      version = "0.1.1",
      author = 'Christian Haudum',
      author_email = 'christian@christianhaudum.at',
      description = 'Supports namespace packages as Django apps.',
      url = 'http://christianhaudum.at',
      packages = find_packages('src'),
      package_dir = {'':'src'},
      install_requires = ['Django'],
      include_package_data = False,
      zip_safe = False,
)

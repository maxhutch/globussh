#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import globussh

setup(name='globussh',
      version=globussh.__version__,
      description='Globus CLI bindings',
      url='http://github.com/maxhutch/globussh/',
      author='https://raw.github.com/maxhutch/globussh/master/AUTHORS.md',
      author_email='maxhutch@gmail.com',
      maintainer='Max Hutchinson',
      maintainer_email='maxhutch@gmail.com',
      license='MIT',
      keywords='globus',
      packages=['globussh'],
      zip_safe=True)

#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

packages = find_packages(exclude=['test'])
requires = ['requests >= 2.0']

__version__ = ''
with open('cine_io/version.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break

if not __version__:
    raise RuntimeError('Cannot find version information')

def data_for(filename):
    with open(filename) as fd:
        content = fd.read()
    return content


setup(
  name="cine_io",
  version=__version__,
  description='cine.io is an api driven platform for creating and publish live streams. The provides cine.io functionality using your given public and secret keys.',
  license='MIT',
  author='Cine.io Engineering',
  author_email='engineering@cine.io',
  url='https://www.cine.io',
  packages=packages,
  package_data={'': ['LICENSE']},
  include_package_data=True,
  install_requires=requires,
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Internet",
  ],
)

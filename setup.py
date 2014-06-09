#!/usr/bin/env python

from setuptools import setup

setup(
    name='cineio-python',
    version='0.1',
    description='cine.io is an api driven platform for creating and publish live streams. The provides cine.io functionality using your given public and secret keys.',
    author='Cine.io Engineering',
    author_email='engineering@cine.io',
    url='https://www.cine.io',
    packages=['cine_io'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet",
    ],
    keywords='networking eventlet nonblocking internet',
    license='MIT',
    install_requires=[
      'setuptools',
      'greenlet',
    ]
    )

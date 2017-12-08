#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open
from setuptools import setup, find_packages

__author__ = 'YangYang'
__author_email__ = 'zhang-yangyang@foxmail.com'
__version__ = '1.0'
__license__ = 'MIT'

here = os.path.abspath(os.path.dirname(__file__))


def long_description():
    try:
        return open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


about = {}
with open(os.path.join(here, 'query', 'config.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__name__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description(),
    author=about['__author__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    platforms=['any'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages=find_packages(),
    package_dir={'query': 'query'},
    package_data={
        '': ['*.py']
    },
    entry_points={
        'console_scripts': [
            'query = query:main',
        ],
    },
)

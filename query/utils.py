#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

__author__ = 'YangYang'
__author_email__ = 'zhang-yangyang@foxmail.com'
__version__ = '0.1'
__license__ = 'MIT'

_ver = sys.version_info

#: Python 2.x
is_py2 = (_ver[0] == 2)

#: Python 3.x
is_py3 = (_ver[0] == 3)


def convert_code(char):
    if is_py2:
        char = char.decode('utf-8').encode('utf-8')
    else:
        if isinstance(char, bytes):
            char = char.decode('utf-8')
    return char

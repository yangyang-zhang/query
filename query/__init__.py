#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from . import config
from .translate import Query


def main():
    if len(sys.argv) == 1:
        return 'Usage: query -h'
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvt:", ["help", "version", "target="])
    except getopt.GetoptError:
        return 'Usage: query -h'
    tolang = 'zh'
    for opt, arg in opts:
        if opt == '-h':
            return config.__doc__
        elif opt in ("-v", "--version"):
            return config.__version__
        elif opt in ("-t", "--target"):
            if arg not in config.supported_language:
                return 'Usage: query -h'
            tolang = arg
    q = ' '.join(args)
    Query(q, tolang).translate()
    return ''

if __name__ == '__main':
    main()
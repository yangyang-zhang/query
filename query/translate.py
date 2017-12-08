#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import hashlib
import json
from collections import OrderedDict
from . import config
from .utils import convert_code, is_py2

__author__ = 'YangYang'
__author_email__ = 'zhang-yangyang@foxmail.com'
__version__ = '0.1'
__license__ = 'MIT'

try:
    from urllib.request import urlopen
    from urllib.parse import quote, urlencode
except ImportError:
    from urllib2 import urlopen, Request
    from urllib import quote, urlencode


class Query(object):
    def __init__(self, q, tolang='zh'):
        self.url = self.check_parameters(tolang, q)

    def translate(self):
        try:
            resp = urlopen(self.url)
            if is_py2:
                result = json.loads(resp.read(), 'utf-8')
            else:
                result = json.loads(resp.read().decode())
        except Exception as e:
            raise Exception('ERROR: Network service error!')
        return self.parse(result)

    def parse(self, result):
        trans_result = result['trans_result'][0]['dst'].encode('utf-8')
        src_result = result['trans_result'][0]['src'].encode('utf-8')
        if os.name == 'posix':
            print("\033[34m ***************************** \033[0m")
            print("\033[31m *{}:{}\033[0m".format(convert_code(src_result), convert_code(trans_result)))
            print("\033[34m ***************************** \033[0m")
        else:
            print("{}:{}".format(convert_code(src_result), convert_code(trans_result)))
        return {'src_result': convert_code(src_result), 'trans_result': convert_code(trans_result)}

    def check_parameters(self, tolang, q):
        self.q = convert_code(q)
        if tolang not in config.supported_language:
            raise Exception('Please check arg: %s' % tolang)
        self.tolang = tolang
        url = self.split_joint_url()
        return url

    def split_joint_url(self):
        sign = config.appid + self.q + str(config.salt) + config.secretkey
        if is_py2:
            sign = hashlib.md5(sign).hexdigest()
        else:
            sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        url_parameter = OrderedDict()
        url_parameter['appid'] = config.appid
        url_parameter['q'] = self.q
        url_parameter['from'] = config.fromlang
        url_parameter['to'] = self.tolang
        url_parameter['salt'] = config.salt
        url_parameter['sign'] = sign
        url = config.api + urlencode(url_parameter)
        return url

if __name__ == "__main__":
    Query('who are you').translate()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    query apple
    query (-h | --help)

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    -t --target     The target language for the specified translation(default=zh)
                    支持的所有语言如下：
                    zh中文  en英语  yue粤语  wyw文言文  jp日语  kor韩语  fra法语
                    spa西班牙语  th泰语  ara阿拉伯语  ru俄语  pt葡萄牙语  de德语
                    it意大利语  el希腊语  nl荷兰语  pl波兰语  bul保加利亚语
                    est爱沙尼亚语  dan丹麦语  fin芬兰语  cs捷克语  rom罗马尼亚语
                    slo斯洛文尼亚语  swe瑞典语  hu匈牙利语  cht繁体中文 vie越南语
"""
import random

__name__ = 'query-cli'
__author__ = 'YangYang'
__author_email__ = 'zhang-yangyang@foxmail.com'
__version__ = '1.0'
__license__ = 'MIT'
__description__ = 'This is a simple, yet powerful command line translator with baidu translate'

appid = '20171206000102744'
secretkey = 'oUQiiAnxPWjehnt18sxQ'
fromlang = 'auto'
salt = random.randint(32768, 65536)

api = "http://api.fanyi.baidu.com/api/trans/vip/translate?"

supported_language = ['zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra', 'spa', 'th', 'ara', 'ru', 'pt',
                      'de', 'it', 'el', 'nl', 'pl', 'bul', 'est', 'dan', 'fin', 'cs', 'rom', 'slo',
                      'swe', 'hu', 'cht', 'vie']

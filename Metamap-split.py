#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

file = open('S2.txt', 'r')  # 打开文件
read_file = file.read()

get2_ = re.findall('<<<<< Phrase(.+?)<<<<< Mappings', read_file, re.S)
for line in get2_:
    get3_ = line.split('\n')
    print(line)


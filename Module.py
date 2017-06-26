#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
a test module

__author__ = 'zhoukaiyin'
"""
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hellow,world')
    elif len(args) == 2:
        print('hellow,%s' % args[1])
    else:
        print('To many argumrnts')


if __name__ == '__main__':
    test()

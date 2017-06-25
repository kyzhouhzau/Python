#!/usr/bin/env python3
# -*- coding:utf-8-*-
# 词频统计
import collections
import re


def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            words_box.extend(re.split(r'[;\.\s]*', line))
        new_words_box = []
        for word in words_box:
            if word.isalpha():
                new_words_box.append(word)
    return collections.Counter(new_words_box)


a = get_words('zhou.txt')
print(a.most_common(20))

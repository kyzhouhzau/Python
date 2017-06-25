# ！/usr/bin/env python3
# -*- coding:utf-8 -*-
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。 提示：计算平方根可以调用math.sqrt()函数

import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        return'bad operand type'
    if not isinstance(b, (int, float)):
        return'bad operand type'
    if not isinstance(c, (int, float)):
        return'bad operand type'

    if a == 0:
        if b == 0:
            if c == 0:
                return'always ok'
            else:
                return'无解'
        else:
            return'x1=x2=%f' % (-c / b)
    else:
        s = 4 * a * c - b ** 2
        if s >= 0:
            x1 = (-b + math.sqrt(s)) / 2 * a
            x2 = (-b - math.sqrt(s)) / 2 * a
            return x1, x2
        else:
            return'has no solution'


r = quadratic(0, 2, 3)
print(r)

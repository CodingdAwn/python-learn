#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 偏函数 可以用于构造带有默认参数的函数
import functools

int2 = functools.partial(int, base=2)
print(int2('100000'))
print(int2('1010'))

int2 = functools.partial(int, base=10)
print(int2('100000'))
print(int2('1010'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
print(max(5, 6, 7))

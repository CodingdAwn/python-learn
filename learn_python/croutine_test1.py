#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect

def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)

    yield a + b + c
# run
sc = simple_coroutine(5)

next(sc)
ret = sc.send(6)
print('<< yield return %s..' % ret)

ret = sc.send(7)
print('<< yield return %s..' % ret)

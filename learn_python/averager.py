#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def average():
    total = 0
    count = 0
    avg = None
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total / count

ag = average()
print(next(ag))
print(ag.send(10))
print(ag.send(20))


import os
import string
import random

kNumberPool = [1, 2, 3]
kOperatorPool = ['+', '-']

print('hello world!')
print('print number pool is %s' % kNumberPool.__str__)
print('number is %d' % kNumberPool[0])

def plus(l, r):
    return l + r

def maxNumber():
    count = len(kNumberPool)
    return kNumberPool[count - 1]

def minNumber():
    return kNumberPool[0]

def randomNumber(last_result):

    return random.randint(1, 3)

print('number begin is %d, end is %d' % (minNumber(), maxNumber()))
r1 = minNumber()
r2 = maxNumber()
print('%d + %d = %d' % (r1, r2, plus(r1, r2)))

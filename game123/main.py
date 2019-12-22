import os
import string
import random

kNumberPool = [1, 2, 3]
kOperatorPool = ['+', '-']

print('hello world!')

def plus(l, r):
    return l + r

def sub(l, r):
    return l - r

def maxNumber():
    count = len(kNumberPool)
    return kNumberPool[count - 1]

def minNumber():
    return kNumberPool[0]

def randomOperator(last_result):
    if last_result == minNumber():
        return '+'
    elif last_result == maxNumber():
        return '-'
    else:
        return random.choice(kOperatorPool)

def randomPlus(last_result):
    left = maxNumber() - last_result
    return random.randint(1, left)

def randomSub(last_result):
    left = last_result - minNumber()
    return random.randint(1, left)

def randomNumber(last_result):
    operate = randomOperator(last_result)
    print('operate is %s' % operate)
    if (operate == '+'):
        return randomPlus(last_result)
    else:
        return randomSub(last_result)

first = random.choice(kNumberPool)
print('first is %d' % first)
second = randomNumber(first)
print('second is %d' % second)


import os
import string
import random

print('hello world!')
kMaxNumber = 3
kMinNumber = 1
kOperatorPool = ['+', '-']
kQuestion = ""
kDiffcult = 5

def plus(l, r):
    return l + r

def sub(l, r):
    return l - r


def randomOperator(last_result):
    if last_result == kMinNumber:
        return '+'
    if last_result == kMaxNumber:
        return '-'
    return random.choice(kOperatorPool)

def randomPlus(last_result):
    left = kMaxNumber - last_result
    return random.randint(kMinNumber, left)

def randomSub(last_result):
    left = last_result - kMinNumber
    return random.randint(kMinNumber, left)

def randomNumber(last_result):
    print('last number is %d' % last_result)
    operate = randomOperator(last_result)
    print('operator this time %s' % operate)
    global kQuestion
    kQuestion += operate

    random_result = 0;
    if (operate == '+'):
        random_result = randomPlus(last_result)
        last_result += random_result
    else:
        random_result = randomSub(last_result)
        last_result -= random_result
    kQuestion += str(random_result)
    return last_result

last = random.randint(kMinNumber, kMaxNumber)
kQuestion += str(last)

for i in range(kDiffcult):
    last = randomNumber(last)

print(kQuestion)

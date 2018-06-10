#!/usr/bin/env python3

#
# reduce map等高阶函数的练习 
#

L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name

L2 = list(map(normalize, L1))
print(L2)

#实现prod()
from functools import reduce
print('实现prod():')
def prod(L):
    return reduce(lambda x, y: x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#实现str2float
print('实现str2float: ')
def str2float(s):
    DIGITS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, \
            '7': 7, '8': 8, '9': 9, '0': 0}
    def char2num(s):
        return DIGITS[s]

    def fn1(x, y):
        return x * 10 + y

    def fn2(x, y):
        return x / 10 + y

    L = s.split('.')
    print('test', L)
    L[1] = '0' + L[1]
    print('L0:', L[0])
    print('L1:', L[1])
    print('L[1][::-1] :', L[1][::-1])
    print('L[1][::1]] :', L[1][::1])
    return reduce(fn1, map(char2num, L[0])) +\
           reduce(fn2, map(char2num, L[1][::-1]))

print('str2float(\'123.456\') =', str2float('123.456'))

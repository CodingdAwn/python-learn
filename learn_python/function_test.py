#!/usr/bin/env python3
#pratice define function

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#my_abs('A')
my_abs(-10)

#练习 返回ax2 + bx + c = 0方程的两个解

import math
def quadratic(a, b, c):
    if a == 0:
        return -c/b
    elif b*b - 4*a*c < 0:
        return None
    elif b*b - 4*a*c == 0:
        return -b/(2*a)
    else:
        return (-b - math.sqrt(b*b - 4*a*c)) / (2*a), \
               (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
#a = float(input('input a:'))
#b = float(input('input b:'))
#c = float(input('input c:'))
#print (quadratic(a,b,c))

#练习不定参数 dict参数
def f1(a, b, c=0, *arg, **kw):
    print ('a =', a, 'b =', b, 'c =', c, 'arg =', arg, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)

#这里args是4个元素的元组 通过结果输出 可以看出 参数是从右开始读的
args = (1,2,3,4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

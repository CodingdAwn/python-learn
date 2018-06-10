#!/usr/bin/env python3

#
# 生成器的练习
#

print('列表生成式')
L = [x *x for x in range(10)]
print(L)
g = (x * x for x in range(10)) 
print('生成器')
print(g)

#遍历生成器的内容
for n in g:
    print(n)

#输出斐波拉切数列
print('输出斐波拉切数列:')
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
#看一下f是什么对象
print(f)

#如果在函数fib中添加yield 函数就变成生成器了
def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'
f2 = fib2(6)
#输出f2 f2现在应该是一个generator了
print('输出f2 f2现在应该是一个generator了:')
print(f2)

#练习杨辉三角
def triangles():
    result = []
    L = [1]
    yield L

    for n in range(9):
        L = [1] + [L[i] + L[i+1] for i in range(n)] + [1]
        yield L

for i in triangles():
    print(i)

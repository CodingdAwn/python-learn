#!/usr/bin/env python3

#遍历字典
d = {'a':1, 'b':2, 'c':3}
print ('遍历key: ')
for key in d:
    print(key)

print ('遍历value: ')
for value in d.values():
    print(value)

print ('遍历key & value: ')
for k, v in d.items():
    print('k:', k, 'v: ', v)

#遍历字符串
print('遍历字符串')
for ch in 'ABC':
    print(ch)

#检查对象是否可以迭代
from collections import Iterable
print ('is \'abc\' can Iterable? ', isinstance('abc', Iterable))
print ('is [1,2,3] can Iterable? ', isinstance([1,2,3], Iterable))
print ('is 123 can Iterable? ', isinstance(123, Iterable))

#使用索引-元素对遍历
print ('使用索引-元素对遍历:')

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#!/usr/bin/env python3
# 列表生成式

print('list(range(1,11)): ')
print(list(range(1, 11)))

#生成[1x1, 2x2, 3x3]
print('生成[1x1, 2x2, 3x3]:')
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

#生成[1x1, 2x2, 3x3]
print('生成[1x1, 2x2, 3x3]:')
print([x * x for x in range(1, 11)])

print('生成列表时添加if语句: ')
print([x * x for x in range(1, 11) if x % 2 == 0])

#双层循环
print('双层循环: ')
print([m + n for m in 'ABC' for n in 'XYZ'])

#输出本地文件名
import os
print([d for d in os.listdir('.')])

#连接字符串
print('生成y=B x=A')
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k,v in d.items()])

#将字符串小写
L = {'Hello', 'World'}
print([s.lower() for s in L])

#最后的练习
print('课后练习')
L = ['Hello', 'World', 18, 'Apple', None]
L2= []
for s in L:
    if isinstance(s, str):
        L2.append(s.lower())
print(L2)

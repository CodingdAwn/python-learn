#!/usr/bin/env python3
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21], key=abs))

print('字符串排序')
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

print('字符串不区分大小写')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print('字符串不区分大小写 并逆序')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,\
        reverse=True))

#练习题
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)

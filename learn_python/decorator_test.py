#!/usr/bin/env python3
def now():
    print('2018-6-6')

#function 有 __name__属性 
print(now.__name__)
f = now
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#python的语法 @
#相当于 now2 = log(now2)
@log
def now2():
    print('2018-6-6:haha')

now2()

#完整的decorator函数
import functools
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*arg, **kw)
        return wrapper
    return decorator

@log2('i wanna test')
def now3():
    print('111111')

now3()

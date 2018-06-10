#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print ('ABC'.encode('ascii'))
print ('中文'.encode('utf-8'))

print (b'ABC'.decode('ascii'))
print (b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print (len('ABC'))
print (len('中文'))

print (len('中文'.encode('utf-8')))

print ('中文测试')

#python中的格式化
print ('Hello, %s' % 'world')

print ('Hi, %s, test 1+2=%d' % ('dAwn', 3))

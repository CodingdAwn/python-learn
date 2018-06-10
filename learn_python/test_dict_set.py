#!/usr/bin/env python3
#dict 就是c++中的hash map
dic = {'A':100, 'B':80, 'C':60}
print (dic)
print (dic['A'])

dic['C'] = 90
print (dic)

print ('D' in dic)

print (dic.get('D', '没有这个key'))

#set 和c++中的一样就是没有重复元素的集合

#练习试用tuple做dict和set的key
t1 = (1,2,3)
t2 = (1, [2,3])
another_dic = {t1:1}
print (another_dic)

#这里可以试用t1做key 但是不可以试用t2 原因1是不可变的 2里面有可变的
another_dic[t2] = 2

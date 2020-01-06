'''
可迭代的对象 都可以使用 for循环 
如str list tuple set dict
'''
str1 = 'abcde'
for x in str1:
	print(x)
print('---str---')
set1 = {1,3,2,2,4}
for s in set1:
	print(s)
print('---set---')
dict1 = {'a':1,'b':2,'c':3}
for k,v in dict1.items():
	print('key:',k,'value:',v)
print('---dict---')

'''
如何判断对象是否可以迭代? 可以使用collections 模块的iterable类型判断
'''
from collections import Iterable
flg = isinstance('abc',Iterable)
print(flg)

'''
如何实现类似java 下标式循环?使用enumerate()  枚举
'''

for i,v in enumerate(str1):
	print('索引:',i,'value:',v)
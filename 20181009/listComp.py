'''
列表生成式: []
'''
l = [x*x for x in range(1,11)]
print(l)

l2 = [m*m for m in range(1,11) if m%2 == 0]
print(l2)

l3 = [m+m for m in 'ABC' for n in 'XYZ' ]
print(l3)

d1 = {'a':1,'b':2,'c':3}
l4 = [k+'='+str(v) for k,v in d1.items()]
print(l4)

#注意!!
str1 = 'aa'
str2 = 33
print(str1,str2,str1+str(str2)) #, 一个空格 +连接符 但是如果2个变量不是str需要类型转换


#生成器: 区别于列表生成式 使用() 同时 列表生成式一次性生成新list 数据占用内存大 
#而生成器中的元素是按照指定的算法推算出来的，只有调用时才生成相应的数据
g = (x*x for x in range(1,11))
print(g)	#l 是一个list  g 是一个生成器 可以使用next打印 但通常不这么做 使用for循环即可
for n in g:
	print(n)

#

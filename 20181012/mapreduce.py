def f(x):
	return x*x
'''
map()方法接收2个参数 一个是 函数 
另一个是 Iterator map将传入的函数 依此作用到序列的每个元素 并将结果作为新的 Iterator返回
'''
m=map(f,[1,2,3,4,5,6])
l = list(m)
print(l)

'''

'''
r = reduce()
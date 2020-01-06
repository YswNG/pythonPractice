#切片操作符 :  如 L[0:3] list 下标0 至3 但不包括3的元素
#如果第一个索引是0可以省略 L[:3]
#切片可以代替一部分的循环操作

L = ['ee','ww','qq']
print(L[0:3])
print(L[:2])
print(L[-2:])

L2 = list(range(101))
L2.pop(0)
print(L2[:10])
print(L2[-10:-1])

print(L2[:10:2])	# 前10个数中每2个取1个 2是下标的间隔 
print(L2[:])	#取所有数
print(L2[::5])	#所有数中 每隔5 取一个

T = (1,2,3,4,5)		#tuple也可以进行切片操作
print(T[:3])

str = 'abcde'		#字符串
print(str[::2])
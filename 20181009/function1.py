import math
#函数的基本定义
def my_fun(a,b,c):
	return a+b-c

print(my_fun(1,2,1))

#函数参数问题
def power(x,n=2):	#参数n给予了默认值 如果不传入n参数 默认为2
	s = 1
	while n>0:
		n-=1
		s*=x
	return s

print(power(5))
print(power(5,2))


def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end([1]))

#可变参数 就是传入参数的个数是可变的 自动组装成一个tuple
def calc(numbers):
	sum = 0 
	for n in numbers:
		sum+=n
	return sum

print(calc([1,2,3,4]))	#传入一个list 
print(calc((1,2,3,4)))	#传入一个tuple

def calc2(*numbers):	# *号使函数接受了一个tuple 可以传入任意个参数 包括0个参数
	sum = 0 
	for n in numbers:
		sum+=n
	return sum

print(calc2(1,2,4))
print(calc2())

list1 = [1,2,3,4]
print(calc2(*list1))	# *表示将这个list1中所有元素作为可变参数传进方法中
print(calc(list1))

#关键字参数 允许传入0个或任意个参数 这些关键字在内部自动组装成一个dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

print(person('jack',30))
print(person('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('jack',30,**extra))	#**表示把extra这个dict 所有的key value用关键字参数传入到函数中的**kw

#命名关键字参数
def person2(name,age,*,city,job):	# *号用于分割 之后的参数为命名关键字参数 起到了限制关键字参数的名称
	print(name,age,city,job)

person2('jack',18,city='beijing',job='engineer') # 命名关键字参数和位置关键字参数的区别是 必须传入参数名
person2('jack',18,city,job) #只有当方法体上的命名关键字参数有默认值时 才可以不用传入

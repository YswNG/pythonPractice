class Person(object):
	'''
	在实际开发中，我们并不建议将属性设置为私有的，
	因为这会导致子类无法访问（后面会讲到）。
	所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
	本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，
	单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻

	'''
	def __init__(self):
		self.__name = 'aaa'    # python中 没有明确规定 私有变量不能访问 在变量前添加_为一种约定
		self._age = None

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self,name):
		self.__name = name

	@property    # 使用property 装饰器 来包装参数的getter
	def age(self):
		return self._age
	

	@age.setter   # setter
	def age(self,age):
		self._age = age

	def play(self):
		if self._age < 12:
			print('{} is playing balls'.format(self.__name))
		else:
			print('{} is learning python'.format(self.__name))
		


def main():
	p = Person()
	p.__name = 'bbb'
	print(p.__name)
	print(p._Person__name)
	p.age = 22
	p.play()
	p.age = 10

	'''
	p.gender = '男' 
	print(p.gender)
	python 是一种动态语言 所以在这里添加了新的属性 gender 
	可以使用__slots__ 限制自定义类型的对象只能绑定某些属性
	通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
	当然也可以对已经绑定的属性和方法进行解绑定

	'''

	# p.name = 'ysw' 没有提供 name的 setter 方法 这里会报错 
	p.play()
	

if __name__ == '__main__':
	main()
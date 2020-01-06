'''
调试的集中方法
1 直接print
2 断言 凡是需要通过print打印出监视值的地方都可以使用assert 断言来代替
'''
'''
def foo(s):
	n = int(s)
	assert n!= 0 ,'n is zero'  #assert 的意思是 如果后面的条件为false 则抛出assertionerror 并打印后面的语句
	return 10/n
def main():
	foo('0')

main()
'''
'''
但实际上 assert 和 print 比 也好不到哪里去 程序上到处充斥着这些代码
相比print 可以使用-0 参数关闭 assert
'''

'''
3 logging
将print替换成 logging  不会像assert抛出异常 可以输出到文件
'''
'''
import logging
logging.basicConfig(level=logging.INFO) #设置日志级别

s='0'
n=int(s)
logging.info('n=%d' % n)
print(10/n)
'''

'''
4 pdb 
启动python的调试器 pdb 让程序以单步方式运行 可以随时查看运行状态

s = '0'
n = int(s)
print(10/n)
#启动命令行  python -m pdb xxx.py  
之后输入n 单步执行 输入q结束debug模式
p查看变量 c继续运行
'''

'''
5 pdb.set_trace()
同样是使用pdb但不需要单步执行 
需要import pdb 在可能出错的地方 输入pdb.set_trace() 同时不需要特殊的命令行参数
'''
import pdb
s = '0'
n = int(s)
pdb.set_trace() 	#运行到此处会自动暂停 类似于打了一个断点
print(10/n)
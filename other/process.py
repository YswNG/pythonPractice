from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep



# 多进程
class MyProcess(object):

	def download_task(self,filename):
		print('启动下载程序,进程号[{0}]'.format(getpid()))
		print('开始下载{0}...'.format(filename))
		time_to_download = randint(5,10)
		sleep(time_to_download)
		print('{0}下载完成!耗时{1}秒'.format(filename,time_to_download))


	def start_process(self):
		start = time()
		# process创建进程对象,通过target传入执行函数,args传入元组类型参数
		p1 = Process(target=self.download_task,args=('xxxx文件.pdf',))
		# start表示启动进程
		p1.start()
		p2 = Process(target=self.download_task,args=('xxxx视频.avi',))
		p2.start()
		# join标识等待进程执行结束
		p1.join()
		p2.join()

		end = time()
		print('总共耗时{0:.2f}秒'.format(end-start))

# 子进程 错误示例
class SlaveProcess(object):
	'''
	结果是ping pong 各输出了10个 why?
	创建进程时,子进程复制了父进程及其所有的数据结构 每个子进程有自己的独立内存空间
	也就是说他们各有一个counter变量 所以各10个

	'''
	counter = 0

	def sub_task(self,string):
		global counter  # 但是这里如果添加self 会报错
		while self.counter<10: # 在class 中 注意添加self
			print(string,end='',flush=True)
			self.counter+=1 # 在class 中 注意添加self
			sleep(0.01)


	def start_sub_process(self):
		Process(target=self.sub_task,args=('Ping',)).start()
		Process(target=self.sub_task,args=('Pong',)).start()



def main():
	# mp = MyProcess()
	# mp.start_process()

	sp = SlaveProcess()
	sp.start_sub_process()



if __name__ == '__main__':
	main()
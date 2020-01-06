'''
错误机制处理
'''
try:
	print('try...')
	raise ZeroDivisionError('myException')	#抛出异常 raise后语句不会执行
	print('result:')
except Exception as e:
	#如果捕获到异常 会执行except中的逻辑
	print('except:',e)	
finally:
	#finally逻辑必定在try后执行
	print('final...')
print('END')	
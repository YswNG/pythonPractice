classmates = ['jj','yy','mm']
print(len(classmates))
print(classmates)

print(classmates[-1]) #获取最后一个索引值可以使用-1 理解为 倒数第一个 那么 -2 则为倒数第二个 以此类推

classmates.append('adam') # 往后添加
classmates.insert(2,'eve') # 往指定索引处插入
classmates.pop() # 删除末尾元素 出栈
classmates.pop(3) # 指定索引处出栈
classmates[1] = 'ysw' #指定索引处修改

L = ['ad',123,True,['a','b']] # list 中的元素类型可以不同 也可以是一个多维list 
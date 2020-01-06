#dict 类似于map 使用{}
d = {'a':3,'b':'BBB','c':(1,'z',['jj','aa'])}
n = d['c'][2][1]
print(n)

#新增一个key 
d['d']='new'
print(d)
#删除一个key pop
d.pop('a');
print(d)
#通过key 获取值
print(d.get('b'))
#修改
d['d']='update'
print(d)

print('-----')
for key,value in d.items():
	print(key)
	print(value)
print('-----')

print('++++++')
for kv in d.items():
	print(kv)
print('++++++')

#set 
s = set([1,2,3,3,2,1])
print(s)
#增 add  
s.add(4)
print(s)

#update 也可以添加 而且参数可以是 list tuple dict等
s.update([1,2,5,3,'afd'],('t'))
print(s)
#删 remove 但是如果元素不存在会报错 
s.remove(3)
print(s)
#discard 也可以删除 元素不存在也不会报错
s.discard(9)
print(s)
#交集 & 并集 |  
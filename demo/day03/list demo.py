#增
a = []
a.append(1)
a.append('12dafeaojl')
#合并
b =[1,5,'ja','hahah']
# 1.print(a+b),此方法会生成一个新的列表


a.extend(b)
print(a)
#删
#pop 弹出，根据下标删除元素。
#默认删除列表中的最后一个元素
a.pop(1)
print(a)
a.pop()
print(a)
# #清空一个列表,直接给空列表。
# # 列表名+clear
# a = []
# a.clear()

#改
#根据下标更改某个元素的值,同时更改多个元素的值
a[1] = '80'
print(a)
a[0],a[1] = 18,8
print(a)
#查
#根据下标查询某个元素的值
print(a[0])
print(a[3])
#遍历（要结合循环使用）
for i in a:
    print(i)

#截取
#截取部分数据
print(a[1:3])
#倒序
print(a[::-1])
#隔着取，跟步长有关
print(a[::2])\
#求列表的长度
print(len(a))
#成员判断
if(3 in a):
    print('存在列表中')
else:
    print('不存在列表中')

#列表和元组的区别
#1，元组中只有一个数据的时候，后边必须带一个逗号，列表则不需要
b = [1]
a =(1,)
print(b)
print(a)
#2,元组中的数据不可修改
a[0]= 1
print(a)

a = (1,[3],5)


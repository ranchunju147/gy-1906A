#字典
#创建
#字典的特性
#1，字典中的key 是唯一的

a = {}
#字典中新增一对数据
a['姓名'] = '欧阳娜拉'
print(a)
#改
a['姓名'] = '张娜拉'
print(a)
a[1] = 333
print(a)
a[(1,2,3)] = 333
print(a)
#删 删除某一个対值，pop的参数只能是key,不能是下标。没有默认值，必须给key值
# a.pop('姓名')
# print(a)
# del a[(1,2,3)]
# print(a)
#清空字典
# a.clear()
# print(a)
#根据key查velue
print(a['姓名'])
#遍历字典（借助循环）
for key in a:
    print(a[key])
#字典合并
#把一个字典合并到另一个字典中
c = {'姓名','王五'}
d = {'年龄','25'}
c.update(d)
print(c)
#两个字典合并，生成一个新的字典
print(dict(c,**d))
print(c)
print(d)

#成员判断

# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# a =[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# a = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
# a = a.replace("''",'"')
# a = a[2:-2]
# print(a)
# a_li = a.split('" , "')
# print(a_li)
# # c = ['C9', 'D6', 'D9', 'H13', 'H9', 'S7']
#
# j = '5,7,9,4,3,4,8,9,6,1,5,6,4,8,9,4,6'
# #截取
# #截取单个字符
# print(j[4])
# #截取其中一串
# print(j[3:9])
# # #倒序排列
# print(j[::-1])
# #只显示数字
# print(j[::2])
# #切片
# print(j.split(","))
# #替换
# print(j.replace('8',"9"))
# print(j.replace(9,8,1))


# #截取网址
# #https://guoyasoft.com/login?redirect=%2Fcheck%2Fopt
# a = 'https://guoyasoft.com/login?redirect=%2Fcheck%2Fopt'
# xieyi=a.split('://')[0]
# a=a.split('://')[1]
# print(xieyi)
# yuming=a[:a.find('/')]
# print(yuming)
# uri=a[a.find('/'):]
# print(uri)

#
# b='http://qa.yansl.com8080/swagger-ui.html#!/PmsProductCategoryController/createUsingPOST_4'
# xy=b.split('://')[0]
# c=b.split('://')[1]
# print(c)
# a=c.find('/')
# ym=print(c[:c.find('/')])
# uri=print(c[c.find('/')+1:])



#按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
def juge_3_2():
    #第一步
    a=input('请输入牌型：')
    a = a.replace("''",'"')
    # print(a)
    a = a[2:-2]
    a_li =a.split('" , "')
    # print(a_li)
    n ={}
    for i in a_li:
        d = i[1:]
        if d in n:
            n[d] += 1
        else:
            n[d] = 1
    # print(n)
    #c=0,i_k 等于3，c=1,e=0,i_k=2,e=1
    c=0
    b=0
    for i_k in n:
        if(n[i_k] == 3):
            c = 1
        if(n[i_k] == 2):
            b = 1
    if(c == 1 and b == 1):
        print("是三带二")
    else:
        print("是王炸")

for i in range(3):
    juge_3_2()

with open ('D:\\softwareData\\Pycharm\\guoya\\demo\\day04\\cars.txt','r') as f:
    #读文件，readlines()作用就是把文件中所有的内容按行读取出来，存到一个list中：read()把整个文件的内容读取出来，存到一个字符串中
    lines = f.readlines()
    print(lines)
    #for循环遍历这个列表
    for line in lines:
        #去掉每一行末尾的换行符
        line = line.replace('\n','')
        print(line)
        #调用一个方法，搬掉牌型是否是3带2
    juge_3_2(line)
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

# def juge_3_2():
#     a = input('请输入牌型：')
#     a = a.replace("''",'"')
#     a = a[2:-2]
#     # print(a)
#     a_li = a.split('" , "')
#     # print(a_li)
#     # c = ['D1','H1', 'H10' , 'H7' , 'S1' , 'S7']
#     a ={}
#     for i in a:
#         d = i[1:]
#         if d in a:
#             a[d] += 1
#         else:
#             a[d] = 1
#         print(a)
#
#     for i_key in a:
#         print(a[i_key])
# #n = 0,i_key=3,n=1,f=0,i_key=2,f=1
#         if(a[i_key] == 3):
#             n = 1
#         if (a[i_key] == 2):
#             f = 1
#     if(n == 1 and f == 1):
#         print(a,"满足3带2")
#     else:
#         print(a,"不满足3带2")
#
# for i in range(3):
#     def juge_3_2():


#open python提供的一个内置函数：作用就是打开一个文件，参数一：文件路径，参数二：文件的打开模式 r 只读，w可写入，a可读可写入
#with open() as f类似于f = open(),他可以在with的代码执行出问题的时候，做一些资源释放工作


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
    #int() 把字符串（只针对数字）强转成数字类型。在字符串前面+int
    #str() 把数字转换成str.





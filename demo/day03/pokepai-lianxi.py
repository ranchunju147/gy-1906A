# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# # # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# # # a =[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# # a = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
# # a = a.replace("''",'"')
# # a = a[2:-2]
# # print(a)
# # a_li = a.split('" , "')
# # print(a_li)
# # c = ['D1','H1', 'H10' , 'H7' , 'S1' , 'S7']
# a ={}
# for i in c:
#     d = i[1:]
#     if d in a:
#         a[d] += 1
#     else:
#         a[d] = 1
#     print(a)
# for key in a:
#     print(a[key])
# if(a[key] == 3)
#     a = 1
# if (a[key] == 2)
#     b = 1
# if(a = 1 and b = 1)
#     print(a,"满足3带2")
# else:
#     print(a,"不满足3带2")

#
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# # ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

def juge_3_2():
    a = input('请输入牌型：')
    a = a.replace("''",'"')
    a = a[2:-2]
    # print(a)
    a_li = a.split('" , "')
    # print(a_li)
    # c = ['D1','H1', 'H10' , 'H7' , 'S1' , 'S7']
    a ={}
    for i in a:
        d = i[1:]
        if d in a:
            a[d] += 1
        else:
            a[d] = 1
        print(a)

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

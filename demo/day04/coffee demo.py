#
# def buy_coffee(numb1,numb2):
#     print("来到咖啡店")
#     cup_nu = numb1
#     print("告诉营业员我要买",cup_nu,"杯")
#     kafei_price = 30
#     money = numb2
#     print("给钱",money)
#     change_money = money - kafei_price*cup_nu
#     print("拿走",cup_nu,"杯咖啡，还剩",change_money,"元钱")
#
# with open("E:\\softwaredata\\python\\gy-1906A\\demo\\day04\\caffee_data") as f:
#     f_li= f.readlines()
#     for line in f_li:
#         line = line.replace("\n","")
#         line_li = line.split(",")
#         buy_coffee(int(line_li[0]), int(line_li[1]))
# #  int()  把字符串转为数字类型
#  str()
        # print(line)
# buy_coffee(15,500)

print(20+60)
print(20*60)
print(20-60)
print(20/60)


def buy_coffees(cash=100,cups=2):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
buy_coffees()
buy_coffees(100,2)
buy_coffees(60)
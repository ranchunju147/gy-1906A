# print(80+80)
# print(80-80)
# print(80*80)
# print(80/80)
#两数相加

def sum(a,b):
    s = a + b
    print(a,'+',b,'=',s)
    return s

sum(3,5)
#3+5+9
sum(sum(3,5),9)

def cha(c,d):
    f = c - d
    print(c,'-',d,'=',f)

cha(10, 5)

def ji(e,h):
    g = e * h
    print(e,'X',h,'=',g)
    return g
#4*5*10
ji(ji(4,5),10)

ji(8,5)

def shang(q,w):
    if (w != 0):
        res = q / w
        print(q, '/', w, '=', res)
    else:
        print('除数不能为零')

shang(20,0)

#有参数，有返回值
def yy(p1,p2,time):
    return '{}约{}{}看电影'.format(p1,p2,time)
print(yy('小明','小红','5点'))

def yy(p1,p2,time):
    return '{a}约{b}{c}看电影'.format(b=p2,c=time,a=p1)
print(yy('小明','小红','5点'))

#无参数，有返回值
def ff():
    return '小明滚出去'
print(ff())
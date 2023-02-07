import math
import turtle as asd
import time


def TULTLE(CHANG, KUAN, GAO):
    number = 1+(int(CHANG/100))
    PEN = asd.Pen()
    print('这个图形与原大小的比例是1:',number)
    PEN.goto(0, (GAO / number))
    PEN.goto((CHANG / number), (GAO / number))
    PEN.goto((CHANG / number), number)
    PEN.goto(0, 0)
    PEN.goto(0, (GAO / number))
    PEN.left(45)
    PEN.forward(KUAN / (2 * number))
    PEN.right(45)
    PEN.forward(CHANG / number)
    PEN.right(135)
    PEN.forward(KUAN / (2 * number))
    PEN.left(180)
    PEN.forward(KUAN / (2 * number))
    PEN.right(135)
    PEN.forward(GAO / number)
    PEN.right(45)
    PEN.forward(KUAN / (2 * number))
    time.sleep(5)
    PEN.goto(0, 0)
    ASDFGHJKL = 0
    ASDFGHJK = 0
    ASDFGHJ = 0
def yuan():
    A = int(input('半径是：'))
    B = int(input('派保留小数点后几位，最多六位，它是：'))
    C = input('单位是：')
    print('面积是：', ((A * A) * round((math.pi), B)), C, '的平方')
    print('周长是：', ((A * 2) * round((math.pi), B)), C)
def yuan_1():
    AA = int(input('半径是：'))
    BB = int(input('高是：'))
    CC = int(input('派保留小数点后几位，最多六位，它是：'))
    DD = input('单位是：')
    EE = (((AA * AA) * round((math.pi), CC)) * 2)
    print('体积是：', (((AA * AA) * round((math.pi), CC)) * BB), DD, '的立方')
    print('表面积是：', (((AA * AA) * round((math.pi), CC)) * BB + ((AA * AA) * round((math.pi), CC)) * 2), DD, '的平方')
    print('侧面积是：', (((AA * AA) * round((math.pi), CC)) * BB), DD, '的平方')
    print('底面积是：', (EE / 2), DD, '的平方')
def number():
    a = int(input('第一个数'))
    b = int(input('第二个数'))
    c = int(input('a的几次方'))
    d = int(input('b的几次方'))
    A_ = a
    B_ = b
    if (d > 0):
        for g in range(1, d):
            if (g == 1):
                e = (b * b)
            else:
                e = (e * B_)
    elif (d == 0):
        e = 1
    else:
        e = -1
    if (c > 0):
        for g in range(1, c):
            if (g == 1):
                f = (a * a)
            else:
                f = (f * A_)
    elif (c == 0):
        f = 1
    else:
        f = -1
    if (a == 0 or b == 0):
        if (a > b):
            x = b
        else:
            x = a
        y = 0
        for i in range(1, (x + 1)):
            if (a % i == 0 and 0 == b % i):
                y = i
        print('最大公因数：', y)
        yy = ((a * b) / y)
        print('最小公倍数：', -1)
        print('它们的积是：', 0)
        print('它们的商是：', -1)
        print('它们的和是：', (a + b))
        print('它们的差是：', (a - b))
        print('a的乘方2是：', -1)
        print('b的乘方2是：', -1)
        print('a的乘方', c, '是：', -1)
        print('b的乘方', d, '是：', -1)
    else:
        pass
    if (a > b):
        x = b
    else:
        x = a
    y = 0
    for i in range(1, (x + 1)):
        if (a % i == 0 and 0 == b % i):
            y = i
    print('最大公因数：', y)
    yy = ((a * b) / y)
    print('最小公倍数：', int(yy))
    print('它们的积是：', (a * b))
    print('它们的商是：', (a / b))
    print('它们的和是：', (a + b))
    print('它们的差是：', (a - b))
    print('a的乘方2是：', (a * a))
    print('b的乘方2是：', (b * b))
    print('a的乘方', c, '是：', f)
    print('b的乘方', d, '是：', e)
def tu_xing():
    PEN = asd.Pen()
    ASDFGHJ = int(input('长'))
    ASDFGHJK = int(input('宽'))
    ASDFGHJKL = int(input('高'))
    if (ASDFGHJKL > 0):
        TULTLE(ASDFGHJ, ASDFGHJK, ASDFGHJKL)
def many_number():
    lol = 0
    many = []
    many_ = int(input('要几个数进行运算'))
    number_s = 1
    lol = int(input('初始数字'))
    for i in range(many_ - 1):
        number_s = number_s + 1
        number_ = int(input('请输入数字'))
        if many_ != (i-1):
            number_x = int(input('符号,1是+,2是-,3是*,4是/'))
            if number_x == 1:
                lol = lol + number_
            elif number_x == 2:
                lol = lol - number_
            elif number_x == 3:
                lol = lol * number_
            elif number_x == 4:
                lol = int(lol / number_)
            else:
                for a in range(20):
                    worry = 1
                    print('worry --------------------------worry----------------------------worry------------------------worry')
                    print(stop)
    if (worry == 1):
        print('=',-1)
    else:
        print('=',lol)
def all_number_0():
    H = 0
    AAAAAAAAAAAAAAAAA = 0
    BBBBBBBBBBBBBBBB = 0
    CCCCCCCCCCCCCCCCCCCCC = 0
    DDDDDDDDDDDDDDD = 0
    DDDDDDDDDDDDDDD = 0
    EEEEEEEEEEE = 0
    a = 0
    b = 0
    c = 0
    d = 0
    A_ = 0
    B_ = 0
    e = 0
    f = 0
    x = 0
    y = 0
    A = 0
    B = 0
    C = 0
    AA = 0
    BB = 0
    CC = 0
    DD = 0
    EE = 0
    no = 0
    ask = 0
def true():
    ask = int(input('想要计算某种类别，请在输入数字加回车，感谢你的配合，如果报错请第一时间告诉我。圆形的面积加周长：0。圆柱的周长：1。两个数的运算：2。画3d图(娱乐)：3。多数运算(news):4。'))
    if ask == 0:
        yuan()
    elif ask == 1:
       yuan_1()
    elif ask == 2:
       number()
    elif ask == 3:
        tu_xing()
    elif ask == 4:
        many_number()
    else:
        pass
true()
print('------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------')
app = int(input('还想循环使用几次'))
if app >= 1:
    for many_number in range(app):
        all_number_0()
        true()
        print('------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------')
all_number_0()

Money = input("请输入带有符号的金额: ")

if Money[-1] in['R','r']:
    U = (eval(Money[0:-1]) / 7.15)
    print("转换后的金额是{:.2f}U".format(U))

elif Money[-1] in['U','u']:
    R = eval(Money[0:-1]) * 7.15 
    print("转换后的温度是{:.2f}R".format(R))

else:
    print("输入格式错误")

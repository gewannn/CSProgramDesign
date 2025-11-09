# 打印出所有的水仙花数
# 水仙花数是指一个三位数，其各位数字的立方和等于其本身
for i in range(100,1000):
    hundred = i // 100
    ten = (i // 10 ) % 10
    one = i % 10
    if hundred ** 3 + ten ** 3 + one ** 3 == i:
        print(i)
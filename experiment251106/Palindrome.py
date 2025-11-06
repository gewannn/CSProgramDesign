n = int(input("请输入一个整数："))
a = n
rn = 0
if n < 0:
    print("请输入自然数")
while a > 0:
    digit = a % 10         
    rn = rn * 10 + digit
    a = a // 10
if n == rn:
    print(n, "是回文数")
else:
    print(n, "不是回文数")

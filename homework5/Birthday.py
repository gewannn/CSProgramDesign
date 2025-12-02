from random import *
def hasSameBirthday(num):
    birthday = []
    for i in range (num):
        b = randint(1, 366)
        if b in birthday:
            return True
        birthday.append(b)
    return False
num = int(input("请输入人数："))
true_count = 0
for i in range(10000):
    if hasSameBirthday(num):
        true_count += 1
prob = true_count / 10000
print(f"人数为{num}时，有两人同一天生日的概率为：{prob}")
import random
x = random.randint(0, 99)
t = 0
while True:
    n = input("猜一个数：")
    if not n.isdigit():
        print("你输入了非整形数")
        continue
    n = int(n)
    if n > x:
        print("遗憾，太大了")
        t += 1
    elif n < x:
        print("遗憾，太小了")
        t += 1
    else:
        print(f"预测{t}次，你猜中了！")
        break

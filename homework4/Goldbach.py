n = int(input("输入一个偶数："))
for i in range(2, n):
    for j in range(2, n):
        if i + j == n:
            print(n, "=", i, "+", j)
            break

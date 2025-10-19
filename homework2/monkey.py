# x_{n+1} = x_n/2 - 1 ；已知 x_10 = 1，反推：x_n = 2*(x_{n+1}+1)
left = 1            # 第10天早晨
for i in range(9):  # 反推9次得到第1天
    left = 2 * (left + 1)
print(left)         # 1534

# 1～9 纵向为乘数、横向为被乘数：1x1=1；下一行到 2x2；以此类推
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}x{j}={i*j}",end=" ")
    print()

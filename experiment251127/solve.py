a = int(input("请输入一元二次方程的第一个系数："))
b = int(input("请输入一元二次方程的第二个系数："))
c = int(input("请输入一元二次方程的第三个系数："))

d = lambda a, b, c : b ** 2 - 4 * a * c
def solve(a, b, c):
    delta = d(a, b, c)
    if delta < 0:
        x1 = x2 = None
    elif delta == 0:
        x1 = x2 = - b / 2 / a
    else:
        x1 = (-b + (d(a, b, c) ** (1/2))) / 2 / a
        x2 = (-b - (d(a, b, c) ** (1/2))) / 2 / a
    return(x1, x2)

x1, x2 = solve(a, b, c)
print(f"方程的根x1 = {x1}, x2 = {x2}")
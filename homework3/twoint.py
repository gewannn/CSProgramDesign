a = int(input("请输入一个整数："))
b = int(input("请输入一个整数："))

x, y = a, b
while y != 0:
    x, y = y, x % y

gcd = x
lcm = a * b // gcd

print(f"最大公约数为：{gcd}")
print(f"最小公倍数为：{lcm}")
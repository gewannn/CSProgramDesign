for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if 5*x + 3*y + z/3 == 100:
            print("公鸡", x, "母鸡", y, "小鸡", z)

score = int(input("请输入成绩："))
if score < 0 or score > 100:
    print("输入不合法，请输入 0~100 之间的整数！")
elif score >= 90:
    print("优")
elif score >= 80:
    print("良")
elif score >= 70:
    print("中")
elif score >= 60:
    print("及格")
else:
    print("不及格")
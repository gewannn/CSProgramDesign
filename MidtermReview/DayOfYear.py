# 输入某年某月某日，判断这一天是这一年的第几天
year, month, day = [int(x)for x in input("请输入年-月-日：").split('-')]
total_days = 0
for m in range(1,month):
    if m in [1,3,5,7,8,10,12]:
       total_days += 31
    elif m in [4,6,9,11]:
        total_days += 30
    elif m == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 29
        else:
            total_days +=28
total_days += day
print(f"{year}年{month}月{day}日 是该年的第{total_days}天。")
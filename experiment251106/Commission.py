i = float(input("请输入本月利润（万元）："))
bonus = 0.0
if i <= 10:
    bonus = i * 0.1
elif i <= 20:
    bonus = 1 + (i - 10) * 0.075
elif i <= 40:
    bonus = 1.75 + (i - 20) * 0.05
elif i <= 60:
    bonus = 2.75 + (i - 40) * 0.03
elif i <= 100:
    bonus = 3.35 + (i - 60) * 0.015
else:
    bonus = 3.95 + (i - 100) * 0.01
print(f"应发放奖金总数为：{bonus:.2f} 万元")
first_year = 100000
for i in range(10):
    money = first_year * 1.05
    print(f"{i}年后，租金会涨到{money}元")

net_income = 0
month_income = 5000
month_count = 0
while net_income < 300000:
    month_count += 1
    if month_count >1:
        month_income *= 1.07
    net_income += month_income
print(month_count)
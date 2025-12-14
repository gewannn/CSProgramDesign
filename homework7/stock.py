import csv
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
plt.rcParams["font.sans-serif"] = ["STHeiti"]
day = []   # 日期
start = [] # 开盘指数值
end = []   # 收盘指数值
rate = []  # 每日涨幅
with open("stock.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for row in reader:
        day.append(row[0])
        open_price = float(row[1])
        close_price = float(row[2])
        start.append(open_price)
        end.append(close_price)
        
        # 修正：计算单个数据的涨幅
        rt = (close_price - open_price) / open_price * 100
        rate.append(rt)
#画折线图
plt.figure(figsize=(8, 5))
plt.plot(day, end, color="red")
ticks = [4025, 4000, 3975, 3950, 3925, 3900, 3875, 3850]
plt.yticks(ticks)
plt.ylabel("价格 （元）")
plt.xlabel("日期") 
plt.legend()
plt.xticks(rotation=45)  # 日期标签旋转45度，避免重叠
plt.tight_layout()
plt.show()

#画直方图
plt.figure(figsize=(8, 5))
plt.bar(day, rate, width=0.8, color="blue")
ticks = [2, 1, 0, -1, -2]
plt.yticks(ticks, [f'{t}%' for t in ticks])
plt.ylabel("涨跌幅")
plt.xlabel("日期") 
plt.legend()
plt.xticks(rotation=45)  # 日期标签旋转45度，避免重叠
plt.tight_layout()
plt.show()
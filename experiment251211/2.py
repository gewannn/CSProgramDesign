import csv
import matplotlib.pyplot as plt
import os
plt.rcParams["font.sans-serif"] = ["STHeiti"] #用黑体不然显示不出中文
os.chdir(os.path.dirname(os.path.abspath(__file__)))
provinces = []
values = []

with open("RegionalGDP.csv", "r", encoding="gbk") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader) 
    for row in reader:
        provinces.append(row[0])
        values.append(float(row[1]))
plt.figure(figsize=(8, 8))
colors = ['red', 'yellowgreen', 'lightskyblue', 'yellow'] #实例图用的四个颜色
plt.pie(
    values,
    labels=provinces,
    autopct="%1.2f%%",   # 显示百分比，保留1位小数
    startangle=0,        # 和实例图开始位置一致
    counterclock=True,   # 和实例图旋转方向一致
    pctdistance=0.9,     # 让百分比更靠边，和实例图更像
)   
plt.tight_layout()
plt.savefig(provinces.png)
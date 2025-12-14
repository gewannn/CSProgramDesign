import csv
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["STHeiti"] #用黑体不然显示不出中文
years = []
gni = []   # 国民总收入
gdp = []   # 国内生产总值
# 读 CSV
with open("gdp.csv", "r", encoding="gbk") as f: #utf-8打不开
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)          # 第一行：['指标','2018年','2019年',...]
    years = header[1:]             # 从第二列开始就是年份
    row1 = next(reader)            # 第二行：国民总收入
    row2 = next(reader)            # 第三行：国内生产总值
    gni = [float(x) for x in row1[1:]]
    gdp = [float(x) for x in row2[1:]]
    years = years[::-1] # 因为csv里是倒序所以再反一下
    gni   = gni[::-1]
    gdp   = gdp[::-1]
# 柱状图
x = list(range(len(years)))
plt.figure(figsize=(8, 5))
plt.bar([i - 0.25 for i in x], gni, width=0.4, label="国民总收入(亿元)", color="#FF7F50")
plt.bar([i + 0.2 for i in x], gdp, width=0.4, label="国内生产总值(亿元)", color="#87CEFA")
plt.xticks(x, years)
plt.title("2018-2022年国民总收入与国内生产总值")
ticks = [1213157.09, 1151804.59, 1090452.09, 1029099.59, 967747.09, 906394.59]
plt.yticks(ticks)          # 把这几个数作为 y 轴刻度
plt.ticklabel_format(style="plain", axis="y")  # 不要科学计数法，会显示什么1e6
plt.ylim(906394.59, 1213157.09)  # y轴的范围，看起来和原图更像
plt.yticks(ticks, [f"{v:,.2f}" for v in ticks]) #使y轴保留两位小数，且三个数字之间有逗号
plt.legend()
plt.savefig("gdp_bar.png")
# 折线图
plt.figure(figsize=(8, 5))
plt.plot(years, gni, marker="o", label="国民总收入(亿元)", color = "#FF7F50")
plt.plot(years, gdp, marker="o", label="国内生产总值(亿元)", color = "#87CEFA")
plt.title("2018-2022年国内生产总值变化折线图")
ticks = [1213157.09, 1151804.59, 1090452.09, 1029099.59, 967747.09, 906394.59]
plt.yticks(ticks)          # 把这几个数作为 y 轴刻度
plt.ticklabel_format(style="plain", axis="y")  # 不要科学计数法，会显示什么1e6
plt.ylim(906394.59, 1213157.09)  # y轴的范围，看起来和原图更像
plt.yticks(ticks, [f"{v:,.2f}" for v in ticks]) #使y轴保留两位小数，且三个数字之间有逗号
plt.legend()
plt.savefig("gdp_line.png")
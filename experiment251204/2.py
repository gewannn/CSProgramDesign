import csv

scores = {"王小明": 87, "李华": 79}
with open("scores.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "成绩"])
    for name, score in scores.items():
        writer.writerow([name, score])

print("写入完成，已生成 scores.csv 文件。")
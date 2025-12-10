import csv, random

with open("dictionary.csv", "r", encoding="gbk") as f:
    reader = csv.reader(f)
    words = [row for row in reader]

selected = random.sample(words, 50)

with open("study.txt", "w", encoding="utf-8") as f:
    for word, meaning in selected:
        f.write(f"{word}: {meaning}\n")

print("✅ 已生成 study.txt，可复制到手机背单词。")

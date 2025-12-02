def WordCount(text):
    text = text.lower()
    for i in ".,!?;:()\"'":
        text = text.replace(i, " ")
    words = text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq
# 主程序
text = input("请输入英文段落：\n")
freq = WordCount(text)
# 字典转成列表、按出现次数排序
items = list(freq.items())
items.sort(key=lambda x: x[1], reverse=True)
# 输出前10个
print("\n出现次数最多的10个单词：")
for word, count in items[:10]:
    print(word, "--", count, "次")

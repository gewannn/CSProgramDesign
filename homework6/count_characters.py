import jieba
import os

def count(novel, characters, output):
    """统计一部小说中主要人物的出现次数"""

    # 1. 读人物列表
    with open(characters, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    # 把人物名加入 jieba 词库，防止被拆开
    for name in names:
        jieba.add_word(name)

    # 2. 读小说全文
    with open(novel, "r", encoding="utf-8") as f:
        text = f.read()

    # 3. 分词
    words = jieba.lcut(text)

    # 4. 计数（只统计在人物表里的词）
    counts = {name: 0 for name in names}
    for w in words:
        if w in counts:
            counts[w] += 1

    # 5. 按出现次数从大到小排序
    sorted_counts = sorted(counts.items(), key=lambda 
                           x: x[1], reverse=True)

    # 6. 写入结果文件
    with open(output, "w", encoding="utf-8") as f:
        for name, cnt in sorted_counts:
            f.write(f"{name}\t{cnt}\n")

    print(f"统计完成：{novel} → {output}")

if __name__ == "__main__":
    # 统计红楼梦
    count("红楼梦.txt", "红楼梦人物.txt", "红楼统计结果.txt")

    # 统计水浒传
    count("水浒传.txt", "水浒传人物.txt", "水浒统计结果.txt")

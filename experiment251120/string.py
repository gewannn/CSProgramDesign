import random
# 生成由 a-z 组成的 1000 个随机字符
s = "".join(chr(ord('a') + random.randint(0, 25)) for _ in range(1000))
# 统计出现次数
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
# 按字母排序输出
for ch in sorted(freq):
    print(f"{ch}: {freq[ch]}")
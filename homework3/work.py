ability = 1.0
for i in range(1,366):
    if i % 7 in [4, 5, 6, 0]:
        ability *= 1.01
print(f"365天后能力值为：{ability:.2f}")
import csv
with open("mnist_test.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # 跳过字段名

    for i, row in enumerate(reader):
        label = row[0]
        pixels = list(map(int, row[1:]))
        print(f"Label: {label}")
        for y in range(28):
            for x in range(28):
                print('#' if pixels[y*28 + x] > 0 
                      else ' ', end='')
            print()
        print("\n" + "-"*20)
        if i == 9:
            break

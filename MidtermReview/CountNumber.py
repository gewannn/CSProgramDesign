# 从键盘输入一个字符串，统计字符串中出现英文字母、数字和其他字符的个数，并输出这三个统计数字
string = input("请输入一个字符串：")
letter = digit = other = 0
for char in string:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digit += 1
    else:
        other +=1
print(f"字母:{letter}数字:{digit}其他:{other}")
N = int(input("请输入一个整型数作为数列的元素个数："))
nums_strings = input("请输入这N个整数(用逗号分隔): ")
strings = nums_strings.split(",")
nums = []
for s in strings:
    nums.append(int(s))

i = 0
#用while求和
while i < N:
    sum_w += nums[i]
    i += 1

#用for求和
for i in range(N):
    sum_f += nums[i]

print(f"用while求和的结果为{sum_w},用for求和的结果为{sum_f}")
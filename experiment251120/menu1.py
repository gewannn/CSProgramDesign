#创建十个菜名作为列表menu的元素
menu = ["红烧肉", "宫保鸡丁", "鱼香肉丝", "麻婆豆腐", "西红柿炒蛋",
        "水煮鱼", "青椒肉丝", "酸辣土豆丝", "回锅肉", "蚝油生菜"]
#在索引位置5和最末位上各添加一个菜单项目
menu.insert(5, "小炒黄牛肉")
menu.append("蒜蓉西兰花")
#创建一个有5个凉菜的列表submenu，并用extend()函数，添加到（2）处理的列表中
submenu = ["拍黄瓜", "口水鸡", "凉拌木耳", "凉拌海带丝", "凉拌三丝"]
menu.extend(submenu)
#原地排序
menu.sort()
#用pop函数取出排序后索引为3的元素并删除
removed = menu.pop(3)
#用in和count判断红烧肉是否存在
print("用in判断红烧肉是否存在:", "红烧肉" in menu)
print("用count判断红烧肉是否存在:", menu.count("红烧肉"))
#用index查找红烧肉首次出现的位置并用remove删除
if "红烧肉" in menu:
    pos = menu.index("红烧肉")
    print("红烧肉首次出现位置：", pos)
    menu.remove("红烧肉")
#取出索引为2到10的元素，并从原列表删除
new_part = menu[2:11]  # 2..10 => [2:11]
del menu[2:11]
print("取出索引为2到10的元素:", new_part)
#迭代显示当前列表menu的所有元素
print("当前 menu:")
for item in menu:
    print(item)
#删除列表对象menu
del menu

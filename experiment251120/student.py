#创建学生信息字典
Student = {"ID": "2025200107202", "Name": "GuanJingyi", "University": "USTS"}
#新增字典项年级
Student["Grade"] = "Freshman"
#分别用items(), keys(), values()显示字典对象中的所有信息
print("items():", list(Student.items()))
print("keys():", list(Student.keys()))
print("values():", list(Student.values()))
#删除“就读学校 University
Student.pop("University", None)
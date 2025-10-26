# 1、程序功能：读取学生名单，随机从中抽取一名。
# 2、运行方式：打开IDLE，File菜单的Open打开当前源文件，按F5键运行；

import os
import random
import time
import threading
import tkinter

path = os.path.dirname(__file__)
os.chdir(path)

win = tkinter.Tk()   # 创建窗口
win.title("抽签程序")
win.geometry("800x400")
win.resizable(False, False)
win.flag = True

# 在窗口中放2个Label标签（滚动显示学号姓名、显示提示文字）
name = tkinter.Label(win, text="?", font=("宋体", 40, "normal"), fg="red")
name.place(x=40, y=80, width=760, height=100)

label = tkinter.Label(win, text="抽签选中者回答问题！", font=("宋体", 30, "normal"), fg="blue")
label.place(x=40, y=200, width=760, height=50)

# 读取文件中的学生信息，文件中每行存放一个学生的学号和姓名
with open("students.txt", "r", encoding="utf8") as fo:
    names = fo.readlines()

# 点击“开始”按钮后，Label 以很快频率随机显示名单
def switch():
    win.flag = True
    while win.flag:
        n = len(names)
        i = random.randint(0, n - 1)
        name["text"] = names[i]
        time.sleep(0.02)

def btnStartClick():  # 按下开始按钮执行
    t = threading.Thread(target=switch)
    t.start()
    btnStart.configure(state=tkinter.DISABLED)   # 开始按钮变灰
    btnStop.configure(state=tkinter.NORMAL)      # 停止按钮恢复

def btnStopClick():   # 按下停止按钮执行
    win.flag = False
    btnStop.configure(state=tkinter.DISABLED)    # 停止按钮变灰
    btnStart.configure(state=tkinter.NORMAL)     # 开始按钮恢复

btnStart = tkinter.Button(win, text="开始", command=btnStartClick)  # 创建开始按钮
btnStart.place(x=260, y=300, width=120, height=80)

btnStop = tkinter.Button(win, text="停止", command=btnStopClick)    # 创建停止按钮
btnStop.place(x=420, y=300, width=120, height=80)
btnStop.configure(state=tkinter.DISABLED)

win.mainloop()  # 进入主循环，等待用户操作

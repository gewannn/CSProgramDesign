from turtle import *

speed(0)

#原代码
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

#盖住白色部分
penup()
goto(100, 5)
pendown()
dot(100, "yellow")

#把红线再描一遍
color("red")
penup()
goto(0, 0)
setheading(0)
pendown()
while True:      
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

done()
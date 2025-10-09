from turtle import *

speed(0)
hideturtle()

dot(400, "red")     
dot(320, "white")
dot(240, "red")
dot(160, "blue")    

penup()
goto(-47, -63)
setheading(36)
color("white")
pendown()
begin_fill()
for i in range(5):
    forward(150)
    left(144)
end_fill()
done()
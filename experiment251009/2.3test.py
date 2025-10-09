from turtle import Turtle, Screen, done

screen = Screen()
screen.tracer(False)   # 关动画，加速

# 1) 原样画花（黄填充 + 红边）
flower = Turtle(visible=False)
flower.speed(0); flower.color('red', 'yellow')
flower.begin_fill()
while True:
    flower.forward(200)
    flower.left(170)
    if flower.distance(0, 0) < 1:
        break
flower.end_fill()

# 2) 只盖“白环”这层（调这个直径就行）
mask = Turtle(visible=False)
mask.speed(0); mask.penup(); mask.goto(100, 5); mask.pendown()
mask.dot(100, 'yellow')     # 120 约等于你截图里的白环直径，按效果微调

# 3) 把红线再描一遍（在最上层）
lines = Turtle(visible=False)
lines.speed(0); lines.pencolor('red')
for _ in range(400):        # 步数多些让线更密
    lines.forward(200)
    lines.left(170)

screen.tracer(True)
done()

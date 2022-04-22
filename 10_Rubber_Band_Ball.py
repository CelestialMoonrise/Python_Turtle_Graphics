import turtle
import random
s = turtle.Screen()
s.setup(width = 1000, height = 800, startx = 0, starty = 0) 

turtle.bgcolor("black") 
turtle.shape("classic") 

turtle.speed(0)
#turtle.color("#DB7093")
turtle.pensize(0.5)

colors = []
for j in range (50):
    cstr = ["#"+''.join([random.choice('ABCDEF0123456789')for i in range(6)])]
    colors.append(cstr)
print(colors)

side = 6
a = 800
for i in range(a):
    turtle.color(colors[i%side])
    turtle.forward(i*7/side)
    turtle.left(90+(360/side)+2)
    turtle.pensize(i*side/300)

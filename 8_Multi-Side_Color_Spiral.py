import turtle
import random
s = turtle.Screen()
s.setup(width = 800, height = 800, startx = 0, starty = 0) 

turtle.bgcolor("#FFF5EE") 
turtle.shape("classic") 

turtle.speed(0)
#turtle.color("#DB7093")
turtle.pensize(1)
radius = 100

size = 0.5


colors = []
for j in range (50):
    cstr = ["#"+''.join([random.choice('ABCDEF0123456789')for i in range(6)])]
    colors.append(cstr)
print(colors)


colors2 = ["#87CEEB", "#8A2BE2", "#FFB6C1", "#FFE4C4", "#191970", "#CD5C5C", "#87CEEB", "#48D1CC"]
side = 12


#turtle.begin_fill()
for i in range(360):
    turtle.color(colors[i%50])
    turtle.pensize(size+0.02)
    turtle.forward(i*6/side+side) #the + gives you the hole
    turtle.left(360/side+side) #轉的角度多籍一點便會交錯
#turtle.fillcolor("#FFC0CB")
#turtle.end_fill()

turtle.penup()
turtle.color("black")
turtle.goto(-50,0)
turtle.pendown()
turtle.write("Multi-Side", font=("Arial", 25, "italic"))
turtle.penup()
turtle.goto(-50,-60)
turtle.write("SPIRAL", font=("Arial", 30))
turtle.hideturtle()

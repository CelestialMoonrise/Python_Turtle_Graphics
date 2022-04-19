import turtle
import random
s = turtle.Screen() #宣告畫布，將在上面製作圖形，並用一個變數紀錄畫布資訊
s.setup(width = 500, height = 500, startx = 0, starty = 0) #設定畫布大小(width(pixel), height(pixel))，設定畫筆起始點

turtle.bgcolor("#FFF5EE") #設定畫部背景顏顏色表示，使用用RGB色碼表
turtle.shape("classic") #turtle = 畫筆 還有"arrow""circle""classic""triangle""square"

turtle.speed(0)
turtle.color("#DB7093") #設定畫筆顏色
turtle.pensize(1)
radius = 100

numofcirs = int(turtle.numinput("Number of Circles", "Please input circles needed in rosette(We recommend 20)", 6)) #Title, 預設值6
size = 1
colors = []
for j in range (30):
    cstr = ["#"+''.join([random.choice('ABCDEF0123456789')for i in range(6)])]
    colors.append(cstr)
print(colors)

turtle.clear()
for i in range(numofcirs):
    turtle.pensize(size)
    turtle.color(colors[random.randint(0, 29)])
    turtle.circle(100)
    turtle.color(colors[random.randint(0, 29)])
    turtle.circle(60)
    turtle.color(colors[random.randint(0, 29)])
    turtle.circle(23)
    
    turtle.left(360/numofcirs)
    
turtle.hideturtle()
#ts = turtle.getscreen() #存下視窗畫面
#ts.getcanvas.postscript(file = "6_Personalized_Rosette.jpg")

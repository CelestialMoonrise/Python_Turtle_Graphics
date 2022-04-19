import turtle
s = turtle.Screen() #宣告畫布，將在上面製作圖形，並用一個變數紀錄畫布資訊
s.setup(width = 500, height = 500, startx = -30, starty = -30) #設定畫布大小(width(pixel), height(pixel))，設定畫筆起始點

turtle.bgcolor("#FFF5EE") #設定畫部背景顏顏色表示，使用用RGB色碼表
turtle.shape("classic") #turtle = 畫筆 還有"arrow""circle""classic""triangle""square"

turtle.speed(0)
turtle.color("#DB7093") #設定畫筆顏色
turtle.pensize(1)

colors = ["#87CEEB", "#8A2BE2", "#FFB6C1", "#FFE4C4"]
pos = [(-150, -130), (-150, 130), (150, 130), (150, -130)]



#for x in range(4):
 #   turtle.penup()
  #  turtle.goto(pos[x%4])
   # turtle.pendown()

for x in range(300):
    turtle.color(colors[x%4])
    turtle.forward(x*2)
    turtle.right(91)

turtle.hideturtle()

#turtle.write("4 Quadri Color Square Spiral", font = ("Times", 30, "italic"))

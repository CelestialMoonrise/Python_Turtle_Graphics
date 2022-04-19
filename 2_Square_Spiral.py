import turtle
s = turtle.Screen() #宣告畫布，將在上面製作圖形，並用一個變數紀錄畫布資訊
s.setup(width = 500, height = 500, startx = -30, starty = -30) #設定畫布大小(width(pixel), height(pixel))，設定畫筆起始點

turtle.bgcolor("#FFE4E1") #設定畫部背景顏顏色表示，使用用RGB色碼表
turtle.shape("classic") #turtle = 畫筆 還有"arrow""circle""classic""triangle""square"

turtle.speed(0)
turtle.color("#DB7093") #設定畫筆顏色
turtle.pensize(2)

for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)

turtle.penup() #提起畫筆
turtle.goto(-123, -150) #定位畫筆
turtle.pendown() #放下畫筆
turtle.write("Square Spiral", font = ("Times", 30, "italic")) #寫字
turtle.hideturtle()

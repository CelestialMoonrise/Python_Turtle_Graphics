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

colors = ["#98FB98", "#90EE90", "#00FF7F", "#20B2AA", "#00FFFF", "#00BFFF", "#4682B4", "#B0E0E6", "#4169E1", "#6A5ACD", "#40E0D0", "#2E8B57", "#008B8B", "#008080", "#0000CD", "#D8BFD8", "#191970", "#1E90FF", "#7FFFD4", "#9ACD32", "#FFD700"]

for i in range(36):
    turtle.circle(radius)
    turtle.left(10)
    turtle.color(colors[random.randint(1, 20)])


turtle.hideturtle()
turtle.write("Rosette")

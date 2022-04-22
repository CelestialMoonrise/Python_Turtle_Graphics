import turtle
import random
import time

def init(w, h, x, y):
    s = turtle.Screen()
    s.title("Have Fun Catching Apples!")
    s.setup(width=w, height=h, startx=x, starty=y)
    turtle.speed(0)
    turtle.tracer(0)     #turn on/off turtle animation: 0:off->show after drawing 1: On->shows animation.
    t = turtle.Turtle()  #引用turtle()函式
    t.hideturtle()
    turtle.addshape("basket", ((-50, 0), (50, 0), (0, -25))) #new a shape named"basket"
    turtle.penup()
    return t

def set_color(bgcolor="black", pencolor="white", pensize=2):
    turtle.bgcolor(bgcolor)
    turtle.color(pencolor)
    turtle.pensize(pensize)
    c1= ["#87CEEB", "#8A2BE2", "#FFB6C1", "#FFE4C4", "#191970", "#CD5C5C", "#87CEEB", "#48D1CC", "white"]
    c2=colors = []
    for j in range (50):
        cstr = ["#"+''.join([random.choice('ABCDEF0123456789')for i in range(6)])]
        colors.append(cstr)
    return(c1, c2)

def graph_clone(tt, shape="circle"):
    obj_turtle = tt.clone()
    obj_turtle.shape(shape)
    obj_turtle.setheading(90)
    obj_turtle.penup()
    obj_turtle.showturtle()
    return(obj_turtle) #return the object made

##Main Program##
t = init(1000, 800, 0, 0, )
#Basket: clone:會擁有turtle()函式中的所有功能 
basket = graph_clone(t, "basket")
basket.ondrag(basket.goto) #把goto函數綁定到鼠標->使滑鼠可拖曳basket
basket.showturtle()

#Apple
apple = graph_clone(t, "circle")
apple.color('red')
#Board
board = graph_clone(t, "square")
board.goto(-300, -300)
board.color("blue")
board.showturtle()

fps = 60 #每30秒->刷新
freq = fps #每秒產生蘋果數
apple_count = [] #產生的apple位置
score = 0


#Basket 
#model = turtle.Turtle() #重新引入turtle的
#model.penup()
#model.hideturtle()

#basket = model.clone()
#basket.shape("basket")
#basket.setheading(90)
#basket.ondrag(basket.goto) #把goto函數綁定到鼠標->使滑鼠可拖曳basket
#basket.showturtle()

#Apple
#apple = model.clone()
#apple.color('red')
#apple.shape("circle")

#Score Board
#board = model.clone()
#board.goto(-300, -300)
#board.color("blue")

while True:
    apple.clearstamps()
    temp = random.randrange(10) #choose num frm 0-39
    if temp==0: #if the num is 0 apple falls
        apple_count.append([random.randrange(-350, 350), 400, 5+random.randrange(10)]) #start_x, start_y, how much the apple falls
    print(temp, apple_count)

    b_x, b_y = basket.pos() #basket position
    for x in apple_count:     #從apple_count拿出一顆蘋果的位置
        x[1]-=x[2]                 #apple 往下掉:x位置不動y位置減少
        apple.goto(x[0], x[1]) #start dropping from the designated place to the designated distance
        apple.stamp()           #也可用clone,但應為只有需要往下

        if abs(x[0]-b_x)<=50 and 0<=x[1]-b_y <=25:  #絕對值aka距離|蘋果的x座標-籃子x座標|<=100 AND (蘋果的Y座標-籃子Y座標)<=25(否則陷入籃子)->add 10 to score
            score+=10
            apple_count.remove(x) 
        elif x[1]<-400: #apple drop to bottom
            score-=100
            apple_count.remove(x)
    board.clear()       #clear scoreboard
    allstr = "SCORE:" + str(score)
    board.write(allstr, font=("SYSTEM", 40, "normal"))
    turtle.update()
    time.sleep(1/fps) #暫停1/fps seconds


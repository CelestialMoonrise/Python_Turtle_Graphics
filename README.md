# Python_Turtle_Graphics
### Exploration of Python Turtle:
Python Turtle is a type of computer graphics called Turtle Graphics. Python Turtle uses a relative cursor(the turtle) to draw or to print words. In this project, I used Python Turtle to create different shapes and figures, I also created an apple catching game using Python Turtle and I was ultimately able to create a clock.

#### References:
1) RGB Color Codes Chart: https://www.rapidtables.com/web/color/RGB_Color.html 
2) Python Library: https://docs.python.org/3/library/turtle.html

#### Figures Created:
* Square Figures: Simple Square, Square Spiral, QuadriColor Square Spiral
* Circle Figures: Circles, Rosette, Circle Spiral
* Multi-Sided Complex Figures(Sunflower, Rubber Band Ball...)

#### Related Projects:
* Apple Catching Game
* Clock with Date and Time

#### Code Examples:
1) Rosette:
~~~python
for _ in range(10):
  turtle.circle(60) #radius of 60px
  turtle.left(36)
~~~
2) Rubber Band Ball with randomized colors!:
~~~python
import turtle
import random #Used to randomize the colors
s = turtle.Screen()
s.setup(width = 1000, height = 800, startx = 0, starty = 0) 
turtle.bgcolor("black") 
turtle.shape("classic") 
turtle.speed(0)
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
~~~

#### Image Examples:
<img src="https://github.com/CelestialMoonrise/Python_Turtle_Graphics/blob/main/Python%20Turtle%20Graphics%202022_4_19%20%E4%B8%8A%E5%8D%88%2009_56_01.png" width=200, height=200 alt="Rosette">
<img src="https://github.com/CelestialMoonrise/Python_Turtle_Graphics/blob/main/Python%20Turtle%20Graphics%202022_4_19%20%E4%B8%8A%E5%8D%88%2010_30_04.png" width=200,height=200 alt="QuadriColor Spiral"><img src="https://github.com/CelestialMoonrise/Python_Turtle_Graphics/blob/main/Python%20Turtle%20Graphics%202022_4_19%20%E4%B8%8B%E5%8D%88%2003_18_59.png" width=200, height=200 alt="Complex Rosette Flower"><img src="https://github.com/CelestialMoonrise/Python_Turtle_Graphics/blob/main/Python%20Turtle%20Graphics%202022_4_20%20%E4%B8%8A%E5%8D%88%2010_17_32.png" width=300 height=150 alt="Complex Figure(Green)">


from turtle import Turtle, colormode
from random import randint
import sys


def randColor():
    return randint(0,255)


def drawTriangle(t,dist):
    t.fillcolor(randColor(),randColor(),randColor())
    t.down()
    t.setheading(0)
    t.begin_fill()
    t.forward(dist)
    t.left(120)
    t.forward(dist)
    t.left(120)
    t.forward(dist)
    t.setheading(0)
    t.end_fill()
    t.up()


def sierpinski(t,levels,size):
    if levels == 0:
        #   Draw triangle
        drawTriangle(t,size)
    else:
        half    = size/2
        levels -= 1
        #   Recursive calls
        sierpinski(t,levels,half)
        t.setpos(t.xcor()+half,t.ycor())
        sierpinski(t,levels,half)
        t.left(120)
        t.forward(half)
        t.setheading(0)
        sierpinski(t,levels,half)
        t.right(120)
        t.forward(half)
        t.setheading(0)


def main(levels = 2, size = 480):
    t = Turtle()
    t.speed(10)
    t.up()
    t.setpos(-size/2,-size/2)
    colormode(255)
    sierpinski(t,levels,size)


if len(sys.argv) == 1:
    main()
elif len(sys.argv) == 2:
    level = int(sys.argv[1])
    main(level)
elif len(sys.argv) == 3:
    level = int(sys.argv[1])
    size  = int(sys.argv[2])
    main(level, size)
else:
    print("Please read the documentation")

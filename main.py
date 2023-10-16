import colorgram
import random
from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

screen.screensize(canvwidth=400, canvheight=300)
col = colorgram.extract('image.jpg', 30)
res=[]
turtle.hideturtle()
for item in range(0, len(col)):
    res.append((col[item].rgb.r, col[item].rgb.g, col[item].rgb.b))

turtle.penup()
start = turtle.position()
turtle.speed("fastest")
for i in range(0,10):
    turtle.setpos(start[0],start[1]+10*i)
    for j in range(0, 10):

        turtle.dot(5,random.choice(res))
        turtle.forward(10)







screen.exitonclick()
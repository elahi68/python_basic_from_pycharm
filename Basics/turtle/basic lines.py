from turtle import *
import turtle as tur

x = (10, 10)
y = (10, 50)

tur.width(10);
tur.pencolor('red')
tur.penup()
tur.goto(x)
tur.pendown()
tur.goto(y)

x = (0, 0)
y = (40, 90)

tur.width(10);
tur.pencolor('blue')
tur.penup()
tur.goto(x)
tur.pendown()
tur.goto(y)



tur.hideturtle()
tur.exitonclick()
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.pensize(70)
colors = ["red", "orange", "yellow", "green", "light blue", "blue", "purple"]

side = int(input("Введи кол-во сторон: "))
x = 80

for i in range(0, side):
    t.pencolor(random.choice(colors))
    # меняем цвет пера случайно из colors
    t.fd(x)  # fd = forward
    t.rt(360 / side)  # rt = right

screen.exitonclick()
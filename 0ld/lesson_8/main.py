# import random  # подтянуть в проект random
# import random as r  # библиотека под именем r.
# from random import randint  # только randint из random
# from random import *  # так лучше не делать
# x = r.randint(0, 100)  # от 0 до 100
# lst = [0, 1, 2, 3, 4, 5]
# element_random = r.choice(lst)  # выбрать
# r.shuffle(lst)  # shuffle - перемешать
#
# print(x)
# print(element_random)
# print(lst)

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.penup()  # поднять ручку
t.goto(-300, 250)  # x(горизонталь), y(вертикаль)
t.pendown()
screen = turtle.Screen()
t.color("dark green", "pink")  # цвет линии, цвет заливки
t.pensize(8)  # толщина пера
# 1 - сама медленная
# 10 - очень быстро
# 0 - максимальна скорость
t.speed(0)  # speed - изменение скорости

goriont = 300
vertical = 200

t.begin_fill()  # начать закрашивание
t.forward(goriont)  # вперед на 50 пикселей
t.right(90)  # поворот направо на 90  градусов
t.forward(vertical)  # вперед на 50 пикселей
t.right(90)  # поворот направо на 90  градусов
t.forward(goriont)  # вперед на 50 пикселей
t.right(90)  # поворот направо на 90  градусов
t.forward(vertical)  # вперед на 50 пикселей
t.right(90)  # поворот направо на 90  градусов
t.end_fill()

t.penup()
t.goto(-100,200 )
t.pendown()
t.fd(50)

t.write("Movavi", font=("Arial Black", 50, "normal"),align="center")
# текст, шрифт=(семейство шрифта, размер стиль)

screen.exitonclick()

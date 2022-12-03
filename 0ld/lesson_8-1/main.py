# import random  # подтянуть в проект библиотеку
# print(random.randint(0, 100))  # 0 <= x <= 100

# import random as r  # r = random
# print(r.randint(0, 100))

# from random import randint  # подтянуть ТОЛЬКО randint из random
# print(randint(0, 100))

# from random import *  # импортировать всё из модуля (ЭТО ПЛОХО)
# print(randint(0, 100))

# import random as r
# lst = [0, 1, 2, 3, 4, 5]
# print(r.choice(lst))  # random.choice - выбрать одно случайное
# r.shuffle(lst)  # random.shuffle - перемешать содержимое
# print(lst)

import turtle
screen = turtle.Screen()  # экран
t = turtle.Turtle()  # черепашка

# t.forward(100)  # fd()
# t.back(100)  # bk()
horizontal = 200
vertical = 100
t.pensize(6)  # размер пера в пикселях
t.color("red", "yellow")
t.speed(1)
t.shape("turtle")
# 1 - медленно
# 10 - очень быстро
# 0 - максимальна

t.begin_fill()  # начало закрашивание
t.fd(horizontal)
t.right(90)  # повернуть направо на 90 градусов
t.fd(vertical)
t.rt(90)  # rt = right
t.fd(horizontal)
t.rt(90)
t.fd(vertical)
t.rt(90)
t.end_fill()

# t.speed(1)
t.penup()  # поднимаем перо
t.goto(120, -40)
t.pendown()  # опустить перо
t.fd(50)
t.circle(30)  # круг с диаметром 30 пикселей
t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")

screen.exitonclick()  # выйти по клику

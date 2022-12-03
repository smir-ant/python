# import random
# print(random.randint(0, 100))

# import random as r
# print(r.randint(0, 100))

# from random import randint
# print(randint(0, 100))

# from random import *  # импортировать всё (лучше не надо)
# print(randint(0, 100))

# spisok = [1, 2, 3, 4, 5]
# print(r.choice(spisok))
# r.shuffle(spisok)  # shuffle - перемешать содержимое
# print(spisok)

# import turtle
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# horizontal = 200
# vertical = 100
# t.color("dark green", "yellow")
# t.pensize(8)
# t.speed(0)
# # 1 - самая медленная скорость
# # 10 - очень быстрая
# # 0 - максимально быстро
#
# t.begin_fill()
# t.forward(horizontal)
# t.right(90)
# t.fd(vertical)  # то же самое, что и forward()
# t.rt(90)  # то же самое, что и right()
# t.fd(horizontal)
# t.rt(90)
# t.fd(vertical)
# t.rt(90)
# t.end_fill()
#
# t.penup()  # поднять перо
# t.goto(120, -30)  # перенесли указатель на координаты
# t.pendown()  # опустить перо
# t.fd(50)
#
# t.circle(50)
# t.color("blue")
# t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")
#
# screen.exitonclick()  # выход при клике

# import random
# import time
# hacked = 0
#
# while hacked < 100:
#     hacked = hacked + random.randint(1, 10)
#     if hacked >= 100:
#         print("Прогресс: 100%")
#     else:
#         print(f"Прогресс: {hacked}%")
#     time.sleep(1)

# import random
# variant = ["1️⃣", "2️⃣", "3️⃣"]
# guess = input("Где шарик? 1️⃣, 2️⃣, 3️⃣\n")
# answer = random.choice(variant)
# if guess == answer:
#     print("Балдёж 😎")
# else:
#     print("Не-а, он был в", answer)

#
# import turtle
# import random
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
# colors = ["red", "blue", "yellow", "pink", "green", "black"]
#
# i = int(input("Введи количество углов:"))
# side = 100
#
# for _ in range(0, i):
#     t.color(random.choice(colors))
#     t.fd(side)
#     t.rt(360/i)
#
# screen.exitonclick()


import time
import random

print("Время пострелять...")
is_game = True
while is_game:
    patron = random.choice([1, 2, 3, 4, 5, 6])
    # print(patron)
    our = random.choice([1, 2, 3, 4, 5, 6])

    print("Заряжаем револьвер")
    time.sleep(3)
    print("Крутим барабан")
    time.sleep(2)
    print("Выстрел через")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    print("*Выстрел*")

    if patron == our:
        print("Смэрть 🌽")
        is_game = False
    else:
        print("Не смэрть 😉")
        if (input("Играем снова?") == "нет"):
            is_game = False


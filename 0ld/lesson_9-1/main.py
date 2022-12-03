# import random
# import time
#
# print("Время пострелять.")
#
# is_game = "y"
# while is_game == "y":
#     time.sleep(0.5)
#     print("*Заряжаем револьвер*")
#     time.sleep(2.5)
#     print("*Раскручиваем барабан*")
#     time.sleep(1.5)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("*Выстрел*")
#
#     slots = [1, 2, 3, 4, 5, 6]
#     patron = random.choice(slots)  # .choice - случайно выбрать
#     our = random.choice(slots)
#
#     if patron == our:
#         print("Есть пробитие 🔫")
#         is_game = "n"
#     else:
#         print("Повезло-повезло 😎")
#         x = input("Играем дальше? y - да, n - нет")
#         if x == "n":
#             is_game = "n"


# ЦИКЛЫ

# for
# lst = ["Антон1", "Антон2", "Антон3", "Антон4"]
# for antoha in lst:
#     print(antoha, end="👍")
#
# print()
# for i in range(0, 10):
#     print("Питон балдёж")

# while
# x = 0
# while x != 10:
#     print(x)
#     x += 1  # то же самое что и x = x + 1

# word = input("Введи слово: ")
# while word:  # если слово != "", то работает
#     print(word)
#     word = word[:-1]

# x = int(input("Введи циферку: "))
# while x:  # если != 0 то работает
#     x -= 1  # то же самое, что и x = x - 1
#     if x % 2 == 0:  # если остаток от деления на 2 == 0
#         print(x, end=" ")

x = int(input("Введи циферку: "))
step = 0
while x != 1:
    step += 1  # то же самое, что step = step + 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = x // 2
    else:
        print(f"{step})", end=" ")
        print(x, " / 2 =", end=" ")
        x = 3 * x + 1
    print(x)
print("Шагов:", step)

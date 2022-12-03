# x = 10
# while x > 0:
#     x = x - 2
#     print(x)

# lst = [0, 1, 2, 3, 4, 5]
#
# for super_anton in lst:  # пробегаемся по всем элементам списка
#      print(super_anton)
#
# for mega_anton in range(0, 10 + 1):
#     print(mega_anton)


# # решение через while
# x1 = int(input("Введи число: "))
# x2 = int(input("Введи число: "))
# #
# # while x1 <= x2:
# #     print(x1, end="🎅")
# #     x1 += 1  # то же самое, что и x1 = x1 + 1
#
# for cool_anton in range(x1, x2 + 1):
#     print(cool_anton)


# number = int(input("Ярусов: "))
# while True:
#     symbol = input("Символ: ").strip()  # убрав пробелы
#     if len(symbol) == 1:  # считаем длину символа
#         break  # получив нужное, выходим из while
#     else:
#         print("Один символ мы хотим.")
# for movavi in range(1, number + 1):
#     print(" " * (number - movavi), end="")
#     print(symbol * movavi, end="")
#
#     print(symbol * movavi)  # правая половина + перенос строки


# x = int(input("Число: "))
# for brawl_stars in range(1, 11):
#     print(x, "x", brawl_stars, "=", x * brawl_stars)

width = int(input("Ширина: "))
height = int(input("Высота: "))

for _ in range(height):  #   от нуля до height (не вкл.) - сработает height раз
    print("# " * width)




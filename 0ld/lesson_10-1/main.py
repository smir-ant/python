# lst = [0, 1, 2, 3, 4, 5]
# for element in lst:
#     print(element)
#
# for i in range(0, 10):
#     print(i)



# x1 = int(input("Введи число:"))
# x2 = int(input("Введи число:"))
#
# # через while
# # while x1 <= x2:
# #     print(x1)
# #     x1 += 1  # то же самое что и x1 = x1 + 1
#
# # через for in range
# for j in range(x1, x2 + 1):
#     print(j)


# number = int(input("Ярусов: "))
# while True:
#     char = input("Символ: ")
#     if len(char) == 1:  # len = length = длина
#         break
#
# for i in range(1, number + 1):
#     # левая половина
#     print(" " * (number - i), end="")
#     print(char * i, end="")
#
#     print(char * i)  # правая половина и перенос строки

# x = int(input("Число: "))
# for k in range(1, 21):
#     print(x, "x", k, "=", x * k)

# width = int(input("Ширина: "))
# height = int(input("Высота: "))
#
# for i in range(0, height):
#     print("A " * width)
#
# while True:
#     try:
#         x = int(input("Ярусов: "))
#         if x < 1:
#             raise Exception("🐏 Да ты баран, положительное хочу.")
#     except ValueError:
#         print("Ну блин.")
#         continue
#     except Exception as error_message:
#         print("Низя.", error_message)
#         continue
#     else:  # если ошибок нет
#         break  # выход из while True
#
# while True:
#     char = input("Символ: ").strip()
#     if len(char) != 1:
#         print("Хочу один символ. И кильку.")
#     else:  # если всё хорошо
#         break  # выход из while True
#
# for super_anton in range(1, x + 1):
#     # левая половина
#     print(" " * (x - super_anton), end="")
#     print(char * super_anton, end="||")
#
#     # правая половина
#     print(char * super_anton)

# x = int(input("Чиселко: "))
# for mega_anton in range(1, 11):
#     print(x, "x", mega_anton, "=", x * mega_anton)


ne_znaiy = int(input("Ширина: "))
zabil = int(input("Высота: "))

for _ in range(0, zabil):
    print("# " * ne_znaiy)





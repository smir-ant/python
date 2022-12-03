# phrase = "я люблю MOVAVI"
# # п - нижний регистр (lower case); П - верхний регистр (upper case).
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.capitalize())  # предложение

# .count() - метод строки для подсчёта вхождений
# word = input("Введи слово: ")
# counter = input("Что будем подсчитывать: ")
# print(word.count(counter), "шт.")

# .replace()
# phrase = "быть или не быть"
# print(phrase.replace("быть", "есть"))

# .split()
# phrase = "мне выпал Леон в бравл старсе"
# print(phrase.split(" "))

# number_1 = int(input("Введи число: "))
# operation = input("Введи операцию ( -, +, /, * ): ")
# number_2 = int(input("Введи число: "))
# oper_list = ["-", "+", "/", "*"]
# if operation in oper_list:
#     if operation == "-":
#         print(number_1 - number_2)
#     elif operation == "+":
#         print(number_1 + number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     else:
#         print(number_1 * number_2)
# else:
#     print("Ошибся ты, чувачелло")

# try:
#     number = int(input("Введи число: "))
#     x = 5 / number
# except ZeroDivisionError:  # обработать исключение деления на 0
#     print("Хочу не ноль!")
# except ValueError:  # неверное значение
#     print("Хочу целые циферки")
# else:  # если ошибок не отловлено
#     print("Я поделил!")
# finally:  # отработает в любом случае
#     print("Меня написал Антон.")

try:
    name = input("Введи имя: ")
    if name == "Антон":
        raise Exception("Это имя запрещено, Антона в обиду не дам! 🚫")
except Exception as error_message:  # сохраняем ошибку как error_message
    print("Щас забаню!")
    print(error_message)
else:
    print("А, ну это можно")

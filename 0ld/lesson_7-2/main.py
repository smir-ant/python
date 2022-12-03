# ZeroDivisionError
# x = 7/0

# TypeError
# x = 15 + "а"

# IndexError
# x = [0, -5.5, "пять"]
# print(x[3])

# SyntaxError
# x = "Привет, я Антон

# ValueError
# int("А")

# NameError
# print(x)

# assert
# def summa(numbers):
#     return sum(numbers)
#
# assert summa([1, 2]) == 3
# assert summa([1, 2]) == 4

# try:
#     div = int(input("Введи число, для деления:"))
#     x = 5/div
# except ZeroDivisionError:  # обработка деления на ноль
#     print("У тебя ошибка деления на ноль!")
# # except Exception:  # обработка любой ошибки
# #     print("Ошибка!")
# except ValueError:
#     print("Впиши циферку, пожалуйста 🙏")
# else:  # else - если ошибок не было
#     print("Всё good")
# finally:  # finally - сработает всегда
#     print("Я проверил и попытался!")
# print("Я сработал")


# lst = []
# try:
#     f = open("file.txt")  # файл помещен в f
# except FileNotFoundError:
#     print("А файла-то нет 😣")
# else:
#     try:
#         for line in f:  # для каждой строчки в файле
#             lst.append(int(line))  # добавить в список число
#     except ValueError:
#         print("Я хочу только цифры :(")
#     else:
#         print("Всё хорошо")
#     finally:
#         f.close()
#
# print(lst)

# try:
#     x = 5/0
# except ZeroDivisionError as error_message:
#     print("Слушай, а вот тут ошибочка возникла", error_message)


# x = input("Введи любое имя:").lower().strip()
# try:
#     if x == "антон":
#         raise Exception("Имя моего препода запрещено")
#         # raise - вызов ошибки
# except Exception:
#     print("Я люблю Movavi, и препода в обиду не дам!")

try:
    x = 5 / 0
except ZeroDivisionError:
    pass  # затычка, ничего

if 5 == 2:
    pass

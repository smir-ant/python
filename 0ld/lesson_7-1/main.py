# ZeroDivisionError
# print(55/0)

# TypeError
# x = 1 + "один"

# IndexError
# lst = ["один", 2, "Антон"]
# lst[3]

# SyntaxError
# if 5 < 0

# NameError
# print(x)

# exit code:
# 0 - всё хорошо
# 1 - ошибка
# -1 - прерывание

# try:  # попытаться
#     number = int(input("Введи число: "))
#     x = 5 / number
#     print(x)
# # except ZeroDivisionError:  # ловим исключения
# #     print("На ноль не дели!!!!!!!!!!!!!!!!!!!!")
# # except ValueError:  # если введём буквы
# #     print("Хачу цифирки")
# except Exception:  # Обработка любой ошибки
#     print("Одна ошибка и ты ошибся 🐺")

# try:
#     name = input("Введи имя: ")
#     if name == "Антон":
#         raise Exception("Это имя под запретом! 🚫")
# except Exception as error_m:  # складываем исключение в error_m
#     print("Я запрещаю вам!", error_m)
# else:  # иначе(если не вызывались исключения)
#     print("Ну вот такое имя можно")
# finally:  # сработает в любом случае
#     print("Ы")
#
# print("Я отработав")
#
# try:
#     number = int(input("Введите число:"))
#     x = 5 / number
# except Exception:
#     pass  # затычка, заглушка
#
# if 3 == 3:
#     pass  # TODO: не забудь дописать и купить молока.
#
# temperature = 365 # я комментарий
# print()

def summa(numbers):  # def - объявить функцию
    return sum(numbers)  # возвращаем сумму чисел

print(summa([1, 2, 3]))  # печатаем рез-т функциюю при [1, 2, 3]
assert summa([1, 2]) == 3
assert summa([1, 2]) == 4

# AssertionError - ошибка если не прошли проверку


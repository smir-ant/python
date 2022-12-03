# Виды ошибок

# ZeroDivisionError: division by zero
# x = 15/0

# TypeError
# x = 15 + "а"

# IndexError: list index out of range
# lst = [10, 5, 3]
# print(lst[3])

# SyntaxError
# if 5 > 0

# ValueError
# x = int("А")

# Коды завершения
# 0 - всё хорошо
# 1 - ошибка
# -1 - прерывание


# assert
# def summa(number: list[int]):
#     return sum(number)
#
# assert summa([1, 3]) == 4  # ошибки не будет
# assert summa([1, 3]) == 5  # ошибка

# try:
#     x = 5/0
# except ZeroDivisionError:
#     print("На ноль делить низя")

# try - попытаться
# except - ожидать ошибки

# try:
#     x = 5/0  # первая ошибка. будет обработана
#     int("x")  # вторая ошибка. не дойдем до неё (
# except ZeroDivisionError:  # обработаем деление на ноль
#     print("Деление на ноль")
# except Exception:  # обработается любая ошибка. но не сработает
#     print("Я обработаю всё.")

# try:  # попытатьс
#     x = int(input("Введи число: "))
# except ValueError:  # обработать ошибку
#     print("Э, уважаемый, хочу цифры!")
# else:  # мы не наткнулись на ошибку
#     print("Ура, победа. Ты не глуп.")
# finally:  # сработает всегда.
#     print("Я отработал.")

# try:
#     name = input("Введите имя: ")
#     if name == "Антон":
#         raise Exception("Антона нельзя")  # вызвать собственную ошибку
# except Exception as error_message:  # сохранить ошибку как error_message
#     print("Одна ошибка и ты ошибся 🐺")
#     print("Ошибка-то фатальная:", error_message)

try:
    x = 5/0
except ZeroDivisionError:
    pass  # пустышка-затычка


if 5 > 3:  # если придумали условие
    pass  # но не придумали что делать

temperatura = 50  # typo
print() # серое - weak warning, пожелание
# x / / 5  # красное - фатальное
# x = int(input("Введи число: "))
#
# if 5 < x < 10:  # двойное неравенство
#     print("Ура")
#
# if x < 10 and x > 5:  # два условия обязательно
#     print("Ура")
#
# if x < 10 or x > 5:  # одно из условий
#     print("Ура")


# Списки
# name_1 = "Тоха"
# name_2 = "Антон"
# name_3 = "Антуан"
# mega_anton = [name_1, name_2, name_3]  # список
#
# # операции со списками:
# mega_anton.append("Тоша")  # добавить элемент в список
# mega_anton.pop(2)  # удалить по индексу
# mega_anton.remove("Тоха")  # удалить по значению
#
# print(mega_anton)

# Индексация несколько раз
# man = [["Антон", "Гриша"], ["Компутеры", "Настолки"], "Мама"]
# print(man[0][1])  # выводим Гришу

# number = float(input("Введи число: "))
# if number < 0:  # если
#     print("Отрицательное")
# elif number > 0:  # иначе если  (else + if)
#     print("Положительное")
# else:  # иначе
#     print("Число, на которое нельзя делить")

# year = int(input("Введи год: "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("Високосненько 😊")
# else:
#     print("Не високосненько 😢")

# number_1 = int(input("Введи первое число: "))
# operation = input("Введи операцию (+, -, /, *, **, |):").strip()
# # .strip() - метод строки, убирающий пробелы нач и кон
# number_2 = int(input("Введи второе число: "))
# lst = ["+", "-", "/", "*", "**", "|"]  # список допустимых операций
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "**":
#         print(number_1 ** number_2)
#     elif operation == "|":
#         print(abs(number_1), abs(number_2))
#         # abs() - получить модуль числа

# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
#
# spisok = [number_1, number_2, number_3]
# print("Максимальное число:", max(spisok))
# print("Минимальное число:", min(spisok))
# # min() - поиск минимума; max() - максимум

ticket = input("Введи номер билета: ")
if len(ticket) == 6 and ticket.isdigit():
    # 6 цифр в билете и это числа(положительные)
    first_half = ticket[:3]  # три первых числа
    last_half = ticket[-3:]  # три последних числа
    first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    last_sum = int(last_half[-3]) + int(last_half[-2]) + int(last_half[-1])
    if first_sum == last_sum:
        print("Счастливый 🎫")
    else:
        print("Не счастливый 💔")
else:
    print("У тебя кепка(отстой)")

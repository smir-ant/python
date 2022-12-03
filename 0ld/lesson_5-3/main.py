# x = 7
# # if x <= 7:
# #     print("Меньше или равно")
# # else:
# #     print("Больше")
#
# print(x == 7)
# print(x < 7)

# x = int(input("Введи число: "))
# if x < 0:
#     print("Отрицательное")
# elif x > 0:
#     print("Положительное")
# else:
#     print("Ноль")

# year = int(input("Введи год:"))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("Високосненько")
# else:
#     print("Не високосненько")

# number_1 = int(input("Первое число: "))
# operation = input("Введи операцию (+, -, *, /): ")
# number_2 = int(input("Второе число: "))
#
# lst = ["+", "-", "/", "*"]  # список возможных операций
# if operation in lst:  # если операция возможна
#     if operation == "+":  # если сложить
#         print(number_1 + number_2)
#     elif operation == "-":  # если вычесть
#         print(number_1 - number_2)
#     elif operation == "/":  # если делить
#         print(number_1 - number_2)
#     else:  # иначе(умножить)
#         print(number_1 * number_2)
# else:
#     print("Написал фигню")

# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
# count_pol = 0  # кол-во положительных
# count_otr = 0  # кол-во отрицательных
#
# if number_1 > 0:
#     count_pol += 1
# elif number_1 < 0:
#     count_otr += 1
#
# if number_2 > 0:
#     count_pol += 1
# elif number_2 < 0:
#     count_otr += 1
#
# if number_3 > 0:
#     count_pol += 1
# elif number_3 < 0:
#     count_otr += 1
#
# print("Положительных:", count_pol)
# print("Отрицательных:", count_otr)

# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
# lst = [number_1, number_2, number_3]
# maxi = max(lst)  # поиск минимума
# mini = min(lst)  # поиск максимума
# print("Самое большое:", maxi)
# print("Самое маленькое:", mini)

# h = int(input("Часы:"))
# m = int(input("Минуты:"))
# s = int(input("Секунды:"))
#
# if (h > 23 or h < 0) or (m > 59 or m < 0) or (s > 59 or s < 0):
#     print("Формат неверный :(")
# else:
#     print("Формат верный :)")
#     print(f"{h}:{m}:{s}")  # hh:mm:ss

# ticket = input("Введи номер билета (6 цифр): ")
# if len(ticket) == 6 and ticket.isdigit():  # isdigit - число ли это
#     # [start:end:step]
#     first_half = ticket[:3]
#     last_half = ticket[-3:]
#     first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     last_sum = int(last_half[0]) + int(last_half[1]) + int(last_half[2])
#     if first_sum == last_sum:
#         print("Билет счастливый :)")
#     else:
#         print("Не повезло :(")
# else:
#     print("Ну ты чет фигню вписал")

# month = input("Введи номер месяца: ").strip()
# # .strip() - убрать пробелы
# if month.isdigit() and 12 >= int(month) >= 1:
#     month = int(month)
#     if 3 <= month <= 5:
#         print("Весна")
#     elif 6 <= month <= 8:
#         print("Лето")
#     elif 9 <= month <= 11:
#         print("Осень")
#     else:
#         print("Зима")

hamsters = int(input("Количество хомяков: "))
if 11 <= hamsters <= 19:
    print("🐹", hamsters, "хомяков")
elif hamsters % 10 == 1:
    print("🐹", hamsters, "хомяк")
elif 2 <= hamsters % 10 <= 4:
    print("🐹", hamsters, "хомяка")
else:
    print("🐹", hamsters, "хомяков")
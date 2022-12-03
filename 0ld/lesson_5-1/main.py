# x = 10
# # if -  если
# # else - иначе
# if x <= 10 or x == 15:  # икс меньше или равно десяти
#     print("Икс не больше 10 или равен 15")
# else:
#     print("Икс больше 10")

# x = 10
# print(x == 10)  # правда = True
# print(x == 5)  # ложь = False


# x = int(input("Введите число: "))
# if x < 0:
#     print("Отрицательное")
# elif x > 0:  # elif - else if = иначе если
#     print("Положительное")
# else:
#     print("Нолик")
#
# year = int(input("Введи год: "))
#
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("Вискокосненько")
# else:
#     print("Не високосненько :(")


# number_1 = int(input("Введи первое число: "))
# operation = input("Введи операцию(+, -, *, /): ")
# number_2 = int(input("Введи второе число: "))
#
# lst = ["+", "-", "/", "*"]  # список допустимых операций
# if operation in lst:  # если операция В списке операций
#     if operation == "+":  # операция сложение
#         print(number_1 + number_2)
#     elif operation == "-":  # операция вычитание
#         print(number_1 - number_2)
#     elif operation == "/":  # операция деление
#         print(number_1 / number_2)
#     else:  # операция умножение
#         print(number_1 * number_2)

#
# number_1 = int(input("Введи первое число: "))
# number_2 = int(input("Введи второе число: "))
# number_3 = int(input("Введи третье число: "))
# counter_plus = 0  # счётчик положительных
# counter_minus = 0  # счётчик отрицательных
# if number_1 > 0:  #  проверяем первое число. если оно положительное
#     counter_plus += 1  # положительное число
# else:  # если оно отрицательное (или ноль :) )
#     counter_minus += 1  # прибавляем счётчик отрицательных
#
# if number_2 > 0:  #  проверяем второе число. если оно положительное
#     counter_plus += 1  # положительное число
# else:  # если оно отрицательное (или ноль :) )
#     counter_minus += 1  # прибавляем счётчик отрицательных
#
# if number_3 > 0:  #  проверяем третье число. если оно положительное
#     counter_plus += 1  # положительное число
# else:  # если оно отрицательное (или ноль :) )
#     counter_minus += 1  # прибавляем счётчик отрицательных
#
# print("Положительных:", counter_plus)
# print("Отрицательных:", counter_minus)

#
# number_1 = int(input("Введи первое число: "))
# number_2 = int(input("Введи второе число: "))
# number_3 = int(input("Введи третье число: "))
#
# lst = [number_1, number_2, number_3]
# mini = min(lst)  # поиск минимального
# maxi = max(lst)  # поиск максимального
#
# print("Минимальное: ", mini)
# print("Максимальное: ", maxi)

ticket = input("Введи номер билета:")
if len(ticket) == 6 and ticket.isdigit():  # ticket.isdigit() - является ли числом
    first_half = ticket[:3]  # первые три числа
    second_half = ticket[-3:]  # последние три числа

    first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    second_sum = int(second_half[0]) + int(second_half[1]) + int(second_half[2])

    if first_sum == second_sum:
        print("Твой билет счастливый!")
    else:
        print("Не повезло(")
else:
    print("Не то ты ввёл!")

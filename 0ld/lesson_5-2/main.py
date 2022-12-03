x = 7

# if x >= 10:  # больше либо равно?
#     print("Я сработал!")
# else:
#     print("Ну я тоже сработав")
#
# phrase = "я карта"
# if phrase == "ya karta":  # равно ли?
#     print("Мы карты!")
#
# game = "dota2"
# if game != "brawl stars":  # не равно?
#     print("ну можно и поиграть")

#
# if x >= 10 and (x == 0 or x == 666):
#     print("Я не выполнюсь хоть и ошибок нет")
# else:
#     print("Ну я тоже сработав")


# number = int(input("Введи число: "))
# if number > 0:
#     print("Положительное")
# elif number == 0:  # elif = else if (иначе если)
#     print("Нулик")
# else:
#     print("Отрицательное")


#
# year = int(input("Введи год: "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("високосненько")
# else:
#     print("не високосненько :(")

# number_1 = int(input("Введи первое число:"))
# operation = input("Введи операцию(-,+,*,/):").strip()  # ввод операции
# # .strip() - убрать пробелы
# number_2 = int(input("Введи второе число:"))
# lst = ["-", "+", "*", "/"]  # список допустимых операций
#
# if operation in lst:  # если операция есть в списке
#     if operation == "-":  # если минус
#         print(number_1 - number_2)
#     elif operation == "+":  # если плюс
#         print(number_1 + number_2)
#     elif operation == "*":  # если умножить
#         print(number_1 * number_2)
#     else:  # в других случаях (делить)
#         print(number_1 / number_2)


# number_1 = int(input("Введи первое число:"))
# number_2 = int(input("Введи второе число:"))
# number_3 = int(input("Введи третье число:"))
#
# counter_pol = 0  # счетчик положительных
# counter_otr = 0  # счетчик отрицательных
#
# # проверка первого числа
# if number_1 < 0:
#     counter_otr += 1  # прибавить к отрицательным
# else:
#     counter_pol += 1  # прибавить к положительным
#
# # проверка второго числа
# if number_2 < 0:
#     counter_otr += 1  # прибавить к отрицательным
# else:
#     counter_pol += 1  # прибавить к положительным
#
# # проверка третьего числа
# if number_3 < 0:
#     counter_otr += 1  # прибавить к отрицательным
# else:
#     counter_pol += 1  # прибавить к положительным
#
# print("Положительных:", counter_pol)
# print("Отрицательных:", counter_otr)


# number_1 = int(input("Введи первое число:"))
# number_2 = int(input("Введи второе число:"))
# number_3 = int(input("Введи третье число:"))
#
# lst = [number_1, number_2, number_3]
#
# maxi = max(lst)  # макимум из lst
# mini = min(lst)  # минимум из lst
# print("Минимальное:", mini)
# print("Максимальное:", maxi)

ticket = input("Введи номер билета(6 знаков):")
if len(ticket) == 6 and ticket.isdigit():  # .isdigit - число ли это(в формате str)
    first_half = ticket[:3]  # сохраняем первые три числа
    last_half = ticket[-3:]    # сохраняем последние три числа

    first_sum = first_half[0] + first_half[1] + first_half[2]  # прибавим 1, 2 и 3 цифры
    last_sum = last_half[0] + last_half[1] + last_half[2]  # прибавим 4, 5 и 6 цифры

    if first_sum == last_sum:
        print("Счастливый билет")
    else:
        print("Ну, не повезло :(")
else:  # если ввод некорректный
    print("Введи нормально, пожалуйста!")

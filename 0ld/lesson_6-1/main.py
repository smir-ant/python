# month = input("Ввидити номмир месица: ")
# if month.isdigit() and 1 <= int(month) <= 12:  # .isdigit() - число ли
#     month = int(month)
#     if 3 <= month <= 5:
#         print("Весныа 🌸")
#     elif 6 <= month <= 8:
#         print("Лето 🍕")
#     elif 9 <= month <= 11:
#         print("Осень 🍂")
#     else:
#         print("Зима ❄")
# else:
#     print("Э, чувачелло, ошибся ты")

# h = int(input("Часы:"))
# m = int(input("Минуты:"))
# s = int(input("Секунды:"))

# if 23 >= h >= 0 and 59 >= m >= 0 and 59 >= s >= 0:
#     print("Формат правильный")
#     print(f"{h}:{m}:{s}")
# else:
#     print("Ошибка")
#     if h > 23 or h < 0:  # если ошибка в часах
#         print("Часы в формате [0, 23]")
#     if m > 59 or m < 0:
#         print("Минуты в формате [0, 59]")
#     if s > 59 or s < 0:
#         print("Секунды в формате [0, 59]")

score = 0

q1 = input("Какого цвета трава?\n"
           "а)Что?, б)Апельсин, в)60 бойцов, г)Зеленая\n"
           "--> ")
if q1 == "г":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()
q2 = input("Сколько ног у стандартных павукофф\n"
           "а)Шесть, б)Семь, в)Восемь, г)Девять\n"
           "--> ")
if q2 == "в":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()

q3 = input("Сколько метров может прорыть крот за одну ночь?\n"
           "а)76, б)8, в)100, г)150\n"
           "--> ")
if q3 == "а":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()

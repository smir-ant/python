# familiya = input("Фамилия:").capitalize()
# imya = input("Имя:").capitalize()
# otchestvo = input("Отчество:").capitalize()
# # capitalize - первая буква заглавная, остальные маленькие
#
# # два варианта одинакового вывода
# print(familiya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchestvo[0]}.")

# x = "abracadabra"
# print(x.count("a"))
# # .count() - подсчет

# x = "hello world anton"
# lst = x.split(" ")
# lst.remove("anton")  # удаление по значению
# lst.pop(0)  # удаление по индексу
# print(lst)

# phrase = input("Введи фразу:")
# find = input("Что меняем:")
# replace = input("На что меняем:")
#
# phrase.replace(find, replace)

# x = input()
# print(x.replace("йо", "ё"))

# alphabet = {
#     " ": " ",
#     "а": "a",
#     "б": "b",
#     "в": "v",
#     "г": "g",
#     "д": "d",
#     "е": "e",
#     "ё": "yo",
#     "ж": "zh",
# }
# x = input("Введи фразу:")
# translate = ""
# for bukva in x:
#     translate = translate + alphabet[bukva]
# print(translate)

# x = input("Почта:")
# temp = x.split("@")
# print("Логин:", temp[0])
# print("Домен:", temp[-1])
#
# x = int(input("Введи число"))
# if x < 0:
#     print("Отрицательное")
# elif x > 0:
#     print("Положительное")
# else:
#     print("Ноль")

year = int(input("Год:"))
# целое деление - //
# остаток от деления - %

if year % 4 == 0 and year % 400 == 0 or year % 100 == 0:
    print("Год високосный")
else:
    print("Год не високосный")





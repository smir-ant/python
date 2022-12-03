# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТ"
#
# print(alphabet[::-1])  # вывод в обратном порядке
# # [start:end:step]

# phrase = "анТОН"
# print(phrase.upper())  # поднять в верхний регистр
# print(phrase.lower())  # опустить в нижний регистр
#
# phrase1 = "я ФрАзА, я КарТА, я КАрта..."
# print(phrase1.capitalize())
#
# familiya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchestvo = input("Отчество: ").capitalize()
# print(familiya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchestvo[0]}.")

# x = input()
# print(x.count('а'))  # кол-во маленьких "а"
# print(x.lower().count('а'))  # кол-во всех букав "а"

# x = input("Введите фразу, разделяя слова запятыми: ")
# lst = x.split(",")  # split - разделить, расколоть
# lst.pop(0)  # удалить первый элемент
# lst.pop(-1)  # удалить последний
# # .remove("Вова") - удалить элемент "Вова"
# # .pop(3) - удалить элемент под индексом 3
# print(lst)

# phrase = input("Введите фразу: ")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
#
# print(phrase.replace(find, replace))

# phrase = input("Введите фразу: ")
# print(phrase.replace("йо", "ё"))

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
#     "з": "z",
#     "и": "i",
# }
# x = input("Введи фразу для транслитерации:")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva]
# print(rus)

# alphabet = {
#     " ": " ",
#     "а": "Арбуз",
#     "б": "Баран",
#     "в": "Виталя",
#     "г": "Горох",
# }
# x = input("Введи фразу чего-то:")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva] + " "
# print(rus)

email = input("Введите почту:")
print(email.split("@"))
login = email.split("@")[0]
domain = email.split("@")[-1]
print("Логин:", login)
print("Домэн:", domain)





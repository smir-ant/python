# familya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchestvo = input("Отчество: ").capitalize()
#
# print(familya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familya} {imya[0]}. {otchestvo[0]}.")

# word = input("Введи фразу/слово: ")
# print("a:", word.count("а"))
# print("aб:", word.count("аб"))

# phrase = input("Введи фразу, разделенную пробелами: ").strip()
# # .strip() - удаляет пробелы в начале и конце строки
# lst = phrase.split(" ")
# print(lst)
# lst.pop(0)  # удалить по индексу
# lst.remove("антона")  # удалить по значению
# print(lst)

# phrase = input("Введи фразу:")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
#
# print(phrase.replace(find, replace))
# # .replace() - замена первого элемента на второй

# x = input()
# print(x.replace("йо", "ё"))

alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
}

phrase = input("Введи фразу: ")
translate = ""
for bukva in phrase:
    translate = translate + alphabet[bukva]
print(translate)

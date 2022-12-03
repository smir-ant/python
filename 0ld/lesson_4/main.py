# x = 'Строка'
# x1 = "Строка"
# # x = x1 - они ничем не отличаются
# name = "Антон\nАнтон\nАнтон"  # первый способ разделять строки
# name1 = '''
# Строка 1
# Строка 2
# Строка 3'''  # второй способ разделять строки
# # print(name)
#
# st = "я большой"
# print(st.upper())
#
# st1 = "Я МАЛЕНЬКИЙ"
# print(st1.lower())
#
# st2 = "я фрАза и хОчУ НАЧИНАТЬСЯ с большой"
# print(st2.capitalize())

#
# familiya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchestvo = input("Отчество: ").capitalize()
#
# print(familiya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchestvo[0]}.")
#
# st = input("Введи слово/фразу: ")
# print(st.count("а"))  # именно маленьких букв
# print(st.lower().count("а"))  # все "а" и "А"

# phrase = input("Введите слова через запятую: ")
# lst = phrase.split(",")
# # удалить по значению = .remove("Строка")
# # удалить по индексу = .pop(0)
# lst.pop(0)
# print(lst)

# phrase = input("Введи строчку:")
# find = input("Что меняем:")
# replace = input("На что меняем:")
#
# print(phrase.replace(find, replace))
# # .replace() - метод для замены; find - то что меняем; replace - то НА что мы меняем

phrase = input("Введи строчку:")
print(phrase.replace("ё","е"))


# lst = ["А","Б","В","Г","Д","Е","Ё","Ж",]
# print(lst[0],lst[1],lst[2],lst[3],lst[4])  # вывести 5 первых элементов
# print(lst[0:5])  # вывести 5 первых элементов
# print(lst[0:5:2])  # вывести 5 первых элементов через одного
# x = "Прювет"
# x[2] = "и"
# print(x)
# x = "Привет"
# print(x[0], x[-1])


# x = input("Введи слово: ")
# temp = x[-1]  # сохраняем последний элемент
# print(x.index(temp) + 1)  # выводим индекс элемента temp
#
# print(len(x))  # вывести длину строки
# x = "C:\Python3\python.exe"
#
# print("Имя файла:", x[11:22])
# print("Имя файла:", x[-10:])
# print("Расширение:", x[-3:])
# print("Имя каталога:", x[3:10])
# print("Полный путь к каталогу:", x[0:10])
# print("Полный путь к каталогу:", x[:10])
#
# x1 = x.split("\\")  # split - разделить, разрезать
# # \\ - потому что это не спец.символ, а обычный символ
# print(x1)
# print("Имя файла:", x1[2])

# chapter_1 = input("Глава 1: ")
# page_1 = input("Страница: ")
# chapter_2 = input("Глава 2: ")
# page_2 = input("Страница: ")
# chapter_3 = input("Глава 3: ")
# page_3 = input("Страница: ")
#
# print(chapter_1.ljust(15) + page_1.rjust(15))
# print(chapter_2.ljust(15) + page_2.rjust(15))
# print(chapter_3.ljust(15) + page_3.rjust(15))

text = "12'345'678"  # -> 12345678
## решение через .split
# temp = text.split("'")
# print(temp)
# temp2 = temp[0] + temp[1] + temp[2]
# print(temp2)
# number = int(temp2)

## решение через срезы
# temp = text[:2] + text[3:6] + text[7:]
# number = int(temp)
# print(temp)

## решение через замену
temp = text.replace("'", "")
number = int(temp)
print(number)

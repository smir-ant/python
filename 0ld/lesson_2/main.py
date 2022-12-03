# a = int(input("a: "))
# first = a // 100
# second = a // 10 % 10
# tretie = a % 10
# print("Последняя цифра:", a % 10)
# print("Первая цифра:", a // 100)
# print("Вторая цифра:", a // 10 % 10)
# print("Сумма цифр числа =", first + second + tretie)

# a = int(input("a: "))
# if a % 2 == 1:
#     a = a + 1
# else:
#     a = a + 2
# print(a)

# d = int(input("d: "))
# r = d/2
# print("Длина = ", d * 3.14)
# print("Площадь = ", 3.14 * r ** 2)

sec = int(input("sec: "))

h = sec // 3600
m = sec % 3600 // 60
s = sec % 3600 % 60 % 60

if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
print(f"{h}:{m}:{s}")




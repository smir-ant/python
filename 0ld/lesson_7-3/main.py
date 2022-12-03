# ZeroDivisionError
# x = 5/0

# TypeError
#  = "а" + 15

# IndexError
# x = [0, -15, "Антон"]
# x[3]

# SyntaxError
# if 5 == 4
#     print()

# NameError
# print(x2)

# assert --> AssertionError
# def summa(numbers):
#     return sum(numbers)
#
#
# assert summa([1, 2]) == 3
# assert summa([1, 2]) == 4


# try - попытаться
# except - отлавливание исключений.
# esle - иначе, если ошибок не было ( если всё хорошо )
# finally - в любом случае

# try:
#     number = int(input())
#     x = 5 / number
# except ZeroDivisionError:
#     print("Слышь ты, низя на нуль делить")
# except ValueError:
#     print("Хочу цифирки")
# except Exception:  # любая ошибка будет обработана
#     print("Блин, ты ошибся, получается!")
# else:  # else - когда всё хорошо 🥰
#     print("Я поделив 👉👈")
# finally:
#     print("Меня написал Антон. Все права защищены.")
#
# print("Я закончил работать.")


# PASS
# try:
#     number = int(input())
#     x = 5 / number
# except Exception:
#     pass  # затычка. ничего не произойдет.

# if 5 == 5:
#     pass  # TODO: купить молока и дописать код

# try:
#     x = input("Введи имя:")
#     if x == "Антон":
#         raise Exception("Антона в обиду не дам")
#         # raise - вызвать исключение, ошибку
# except Exception as error_message:
#     # as - сохранить ошибку в error_message
#     print("Это слово запрещено!", error_message)


ints = []
try:
    f = open("text.txt")
except FileNotFoundError:
    print("Ну, не получилось 😒")
else:
    try:
        for line in f:
            ints.append(int(line))
    except ValueError:
        print("Тут не число, закрой за мной дверь, я ухожу.")
    else:  # если ошибок неть
        print(ints)
    finally: # ваще всегда
        f.close()
        print("Я закрыв фаел 😃")
import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)  # число -> строчку

while life:  # то же самое, что и while life != 0
    is_guessed = False  # отгадано?
    print("=" * 10)

    # print("Жизней:", life)
    print("Жизней: ", end="")
    for _ in range(life):
        print("❤", end="")
    print()

    guess = input("Предположение: ")
    if len(guess) != length or not guess.isdigit():  # если длина != 3 или не число
        print("Число от 100 до 999, пожалуйста!")
        continue

    # проверка правильного ответа
    if guess == answer:
        print("Пабеда 🏆")
        is_guessed = True
        break  # выйти из while

    if is_guessed == False:  # если не отгадано
        # проверка на fermi
        for i in range(length):  # от 0 до 2 включительно
            if guess[i] == answer[i]:  # совпадение значения и позиции
                print("Fermi 😎")
                is_guessed = True
                break  # выход из for

    if is_guessed == False:  # не отгадано и не fermi
        # проверка на pico
        for char in guess:
            if char in answer:  # есть ли число в ответе
                print("Pico 😉")
                is_guessed = True
                break  # выход из for

    if is_guessed == False:  # не отгадано и не fermi и не pico
        print("Bagels 😓")

    life -= 1
print(answer)









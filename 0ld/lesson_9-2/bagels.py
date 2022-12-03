import random

length = 3
life = 10

answer = random.randint(100, 999)
answer = str(answer)  # число -> строчку
answer = list(answer)  # строчка -> список

print(answer)


while life:  # while life != 0
    is_guessed = False  # отгадано?

    print("=" * 10)
    # print("Жизней:", life)
    print("Жизней:", end=" ")
    for _ in range(0, life):
        print("♥", end="")
    print()  # разрыв

    guess = input("Предположение: ")
    if len(guess) != 3 or not guess.isdigit():
        # если длина не равна 3 или это не число
        print("Число от 100 до 999, пожалуйста!")
        continue

    if list(guess) == answer:
        print("Победа!")
        is_guessed = True
        break  # выход из while

    if not is_guessed:  # если не отгадал
        for i in range(0, length):
            if guess[i] == answer[i]:  # совпадение позиции и значения
                print("Bagels! 😎")
                is_guessed = True
                break  # выход из for

    if not is_guessed:  # если не отгадал и не bagels
        for char in guess:
            if char in answer:  # совпадение значения
                print("Fermi. 😏")
                is_guessed = True
                break  # выход из for

    if not is_guessed:  # если не отгадал и не bagels, и не fermi
        print("Pico ☹")  # Вообще мимо

    life -= 1  # то же самое что и life = life - 1

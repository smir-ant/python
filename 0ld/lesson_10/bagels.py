import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)  # перевели в тип данных строка

while life:  # пока жизни != 0
    is_guessed = False
    print("=" * 10)

    print("Жизней: ", end="")
    for _ in range(life):
        print("♥", end="")
    print()  # перенос строки

    guess = input("Предположение: ")
    if len(guess) != length or not guess.isdigit():  # если длина != 3 или не число
        print("Число от 100 до 999")
        continue  # перезапускаем цикл

    if guess == answer:  # проверка правильного ответа
        print("Пабеда 🏆")
        is_guessed = True
        break

    if not is_guessed:  # если не отгадал
        # проверка на fermi
        for i in range(length):  # от 0 до 2 включительно
            if guess[i] == answer[i]:  # если совпадает значение и позиция
                print("Fermi 😎")
                is_guessed = True
                break

    if not is_guessed:  # если не отгадал
        # проверка на pico
        for char in guess:  # для каждого символа в guess
            if char in answer:  # если число в ответе
                print("Pico 😉")
                is_guessed = True
                break

    if not is_guessed:  # если не отгадал
        # не было fermi, ни pico
        print("Bagels 😔")

    life -= 1  # life = life - 1
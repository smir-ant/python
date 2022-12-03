import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = "y"
score = 0
while is_game == "y":
    computer = [random.choice(cards)]
    player = [random.choice(cards)]

    get_card = "y"
    while get_card == "y":
        player.append(random.choice(cards))  # append - добавить в список
        if sum(player) > 21 and 11 in player:
            """если туз в руке и сумма > 21"""
            for i in range(0, len(player)):  # пробегаемся по списку по индексам
                if player[i] == 11:
                    player[i] = 1
                    break
        score = sum(player)
        print(f"Твоя рука: {player}. Очков: {score}")
        print("Первая карта компьютера:", computer[0])
        if score > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту, n - остановиться: ")

    while sum(computer) < 17:  # пока у компьютера < 17
        computer.append(random.choice(cards))

    if sum(computer) > 21 and 11 in computer:
        """если туз в руке и сумма > 21"""
        for i in range(0, len(computer)):  # пробегаемся по списку по индексам
            if computer[i] == 11:
                computer[i] = 1
                break
    score_computer = sum(computer)
    print("=" * 10)
    print(f"Твоя итоговая рука: {player}. Очков: {score}")
    print(f"Итоговая рука компьютера: {computer}. Очков: {score_computer}")


    # кто победил
    if score > 21 and score_computer > 21:
        print("Перелёт у обоих. Ничья.")
    elif score > 21:
        print("Твой перелёт. Ты проиграл.")
    elif score_computer > 21:
        print("Перелёт компьютера. Ты победил.")
    elif score == score_computer:
        print("Ничья")
    elif score > score_computer:
        print("Победа.")
    else:
        print("Проиграл")

    is_game = input("Играем дальше? y - да, n - нет")
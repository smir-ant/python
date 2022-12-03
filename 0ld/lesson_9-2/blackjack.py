import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_player = [random.choice(cards)]
hand_computer = [random.choice(cards)]
score_player = 0
score_computer = 0
get_card = "y"
while get_card == "y":
    hand_player.append(random.choice(cards))

    if sum(hand_player) > 21 and 11 in hand_player:
        # если сумма карт > 21 и туз в руке
        for i in range(0, len(hand_player)):  # len() - длина
            if hand_player[i] == 11:  # если карта == тузу
                hand_player[i] = 1
                break

    score_player = sum(hand_player)
    print(f"Твоя рука: {hand_player}. Очков: {score_player}.")
    print(f"Первая карта диллера: {hand_computer[0]}.")
    if score_player > 21:
        get_card = "n"  # если перебрано, то не берем карту 😀
    else:
        get_card = input("🃏 Добираем карту? y - да, n - нет")

while sum(hand_computer) < 17:
    hand_computer.append(random.choice(cards))

    if sum(hand_computer) > 21 and 11 in hand_computer:
        # если сумма карт > 21 и туз в руке
        for i in range(0, len(hand_computer)):  # len() - длина
            if hand_computer[i] == 11:  # если карта == тузу
                hand_computer[i] = 1
                break

score_computer = sum(hand_computer)
print("=" * 10)
print(f"Рука диллера: {hand_computer}. Очков: {score_computer}")
print(f"Твоя рука: {hand_player}. Очков: {score_player}.")

if score_player > 21 and score_computer > 21:
    print("Перелёт обоих. Ничья.")
elif score_player > 21:
    print("Твой перелёт. Проиграл.")
elif score_computer > 21:
    print("Перелёт компутера. Победа.")
elif score_player == score_computer:
    print("Ничья.")
elif score_player > score_computer:
    print("Победа.")
else:
    print("Проиграл.")

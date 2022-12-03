import os

total_bets = []
triger = "yes"

while triger == "yes":
    name = input("Имя: ")
    bet = int(input("Ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)
    triger = input("yes - продолжаем, no - останавливаем")
    os.system("cls||clear")

winner = {'name': '', "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["bet"] > winner['bet']:  # если ставка больше чем у победителя
        winner["name"] = total_bets[i]['name']  # перезаписываем имя победителя
        winner["bet"] = total_bets[i]['bet']  # перезапись ставки победителя

print(f"Победитель: {winner['name']}. Его ставка: {winner['bet']}.")



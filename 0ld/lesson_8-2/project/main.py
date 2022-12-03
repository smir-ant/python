import additional
import random

print(additional.logo)

score = 0
data = additional.data

is_game = True
while is_game:
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print("Твой счёт:", score)
    print("-" * 10)
    print(f"А: {a['name']}. {a['description']} из {a['country']}")
    print(additional.vs)
    print(f"B: {b['name']}. {b['description']} из {b['country']}")
    select = input("У кого больше подписоты? (A, B, МЕНЯЙ)").upper().strip()
    if select == "МЕНЯЙ":
        continue
    if select == "A" or select == "B":
        if a["follower_count"] > b["follower_count"] and select == "A":
            score = score + 1
            print("Праильна!")
        elif a["follower_count"] < b["follower_count"] and select == "B":
            score = score + 1
            print("Праильна!")
        else:
            print("Одна ошибка и ты ошибся 🐺")
            is_game = False
    else:
        print("Я обиделся")
        quit()


import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерирем? (до 65)")
    if not number.isdigit() or int(number) > 65 or int(number) < 2:  # валидация значения
        print("Это по-твоему смешно? Нормально введи, пожалуйста.")
        print("-------")
    else:  # правильно ввели
        number = int(number)  # преобразование в число
        break

birthdays = []
startOfYear = datetime.date(2022, 1, 1)  # 2022 год, 1 месяц, 1 день
for _ in range(number):  # отработает number раз
    randomNumberOfDays = datetime.timedelta(random.randint(0, 364))  # случайный сдвиг
    birthday = startOfYear + randomNumberOfDays  # случайный др = старт года + сдвиг
    birthdays.append(birthday)

for i in range(number):
    print(f"{i + 1}) {birthdays[i]}")

print("=" * 10)
for i in set(birthdays):  # пробегаемся по множеству(убрав повторения)
    if birthdays.count(i) > 1:  # если дня рождения > 1 штук
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.")



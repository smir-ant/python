import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерим?")
    if not number.isdigit() or int(number) < 2:
        print("Это по-твоему смешно? Число от.")
        print("=" * 10)
    else:
        number = int(number)  # преобраование в число
        break  # выход из while

birthdays = []
startOfYear = datetime.date(2022, 1, 1)  # год, месяц, день

for _ in range(number):
    # случайный сдвиг
    shiftOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfYear + shiftOfDays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays):  # set = множество, повторения исключены
    if birthdays.count(i) > 1:  # i втречается 2+ раза
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.")










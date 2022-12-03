import random
import datetime

while True:
    number = input("Сколько дней рождения генерируем? (до 70)")
    if not number.isdigit() or int(number) < 2 or int(number) > 70:
        print("Это по-твоему смешно? Введи от 2 до 70, пж 🥺")
        print("-" * 5)
    else:
        number = int(number)
        break  # выход из while True

birthdays = []
startOfYear = datetime.date(2022, 1, 1)
for _ in range(number):
    sdvig = random.randint(0, 364)
    randomDay = datetime.timedelta(sdvig)
    birthday = startOfYear + randomDay
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index].strftime('%d.%m.%y')}")
    # .strftime() - string format time - поменять формат

print("=" * 10)
for i in set(birthdays):  # список -> множество. исключение повторений
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза")

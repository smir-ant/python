import datetime

MONTHS = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
DAYS = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

while True:
    year = input("Год: ")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break

while True:
    month = input("Месяц: ")
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break

calText = ""
calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

for i in range(7):
    calText += DAYS[i] + " "
calText += "\n"

weekSeparator = ("+----------" * 7) + "\n"
blankRow = ("|          " * 7) + "|\n"

currentDate = datetime.date(year, month, 1)  # первый день нужного месяца
while currentDate.weekday() != 0:  # пока не понедельник
    currentDate -= datetime.timedelta(days=1)  # отнимаем 1 день

while True:
    calText += weekSeparator
    dayNumberRow = ""
    for i in range(7):
        dayNumberLabel = str(currentDate.day).rjust(2)  # число
        dayNumberRow += "|" + dayNumberLabel + (" " * 8)  # ряд(ячейка)
        currentDate += datetime.timedelta(days=1)  # переходим к сл. дню
    calText += "|\n"
    calText += dayNumberRow
    for i in range(3):
        calText += blankRow

    # закончили ли мы обработку месяца
    if currentDate.month != month:
        break

calText += weekSeparator
print(calText)

calendarFileName = 'calendar_{}_{}.txt'.format(month, year)
with open(calendarFileName, "w") as file:
    file.write(calText)

print('Сохранено в ' + calendarFileName)

import random
import hangman_art as art

print(art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary)
word_display = []

for _ in range(len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0  # кол-во проявленных букв

while life > 0 and counter != len(word_answer):
    print(art.stages[life])
    letter_is_be = False  # наличие буквы в слове

    # пока проявленных != букв в ответе и жизней > 0
    letter = input("Буква: ").lower()
    for i in range(len(word_answer)):  # пробегаемся по ответу
        if letter == word_answer[i]:  # если буква
            if word_display[i] != "_":  # если буква отгадана
                letter_is_be = True
            else:  # если буква не отгадана
                word_display[i] = letter  # переворачиваем букву
                counter += 1  # +1 проявленная буква
                letter_is_be = True
    if letter_is_be == False:  # если мимо
        life -= 1
    print(word_display)

if counter == len(word_answer):
    print("Пабеда 🎉")
else:
    print(art.stages[life])
    print("Не получилос.")
    print(word_answer)

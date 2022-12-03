intro = """
   ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██                  ▓▀▓
   ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█                 ▓▌ ▐▓ 
   ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█                ▓▌▄▄▄▐▓ 
   ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█               ▓▌     ▐▓
   ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀  ▄▄▄▄▄▄▄▄▄▄  ▐█       █▌
"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(intro)

import random

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary).lower()  # перевели в маленькую букавку
word_display = []
for i in range(0, len(word_answer)):
    word_display.append("_")
print(word_answer)

counter = 0  # счётчик угаданных букв
life = 6
print(word_display)

while counter != len(word_answer) and life > 0:  # играем пока все буквы е отгаданы и пока жизней > 0
    print(stages[life])
    letter = input("Буква:")
    letter_is_be = False  # наличие буквы в слове
    for i in range(0, len(word_answer)):
        if letter == word_answer[i]:  # если буква равна букве из ответа
            if word_display[i] != "_":  # если буква отгадана
                letter_is_be = True
            else:
                word_display[i] = letter  # открываем букву
                counter += 1
                letter_is_be = True
    if not letter_is_be:
        life = life - 1
    print(word_display)


if counter == len(word_answer):
    print("Пабеда")
else:
    print(stages[life])
    print("Не победа :(")

# pastebin.com/g85iHYnF


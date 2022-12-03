import random
import viselica_art

print(viselica_art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary).lower()
word_display = []

for _ in range(len(word_answer)):  # выполним букв_в_слове раз
    word_display.append("_")

print(word_display)
life = 6
counter = 0  # счётчик проявленных букв

while life > 0 and counter != len(word_answer):
    print(viselica_art.stages[life])
    # пока есть жизни и не все буквы отгаданы
    letter = input("Буква: ")
    letter_is_be = False  # наличие буквы в слове
    for i in range(len(word_answer)):  # пробегаемся по слову
        if letter == word_answer[i]:  # если буква равна букве из слова
            if word_display[i] != "_":  # если буква уже перевернута
                letter_is_be = True
            else:
                word_display[i] = letter  # переворачиваем букву
                letter_is_be = True
                counter += 1  # то же самое, что и counter = counter + 1

    if letter_is_be == False:  # если буквы найдено не было
        life -= 1
    print(word_display)
if counter == len(word_answer):
    print("Пабеда")
else:
    print(viselica_art.stages[life])
    print("Проиграв")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

while not should_end:  # пока should_end != True
    text = input("Введи сообщение: ")
    text = list(text)  # строчка -> список
    shift = int(input("Сдвиг: "))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    elif shift < -len(alphabet):
        shift = shift % -len(alphabet)

    # механизм сдвига
    cipher_text = ""
    for letter in text:
        if letter == " ":
            cipher_text += letter  # добавляем пробел как он есть
        else:
            position = alphabet.index(letter)  #  какой index у letter
            if position + shift > len(alphabet):  # вышли за верх
                new_position = position + shift - len(alphabet)
            elif position + shift < 0:  # вышли за низ
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]

    print(cipher_text)
    restart = input("Ещё раз? y - да, n - нет")
    if restart == "n":
        should_end = True


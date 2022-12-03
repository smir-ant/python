alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['(', ')', ',', '.', ' ', '!', '?']

should_end = False
while not should_end:  # пока should_end != True
    text = input("Введи свое сообщение: ").lower()
    text = list(text)  # преобразовать в список
    shift = int(input("Введи сдвиг:"))

    if shift > len(alphabet):  # сдвиг > длины алфавита
        shift = shift % len(alphabet)  # сдвиг 100 = сдвиг 22
    elif shift < -len(alphabet):  # сдвиг меньше -длина алфавита
        shift = shift % -len(alphabet)

    # механизм сдвига
    cipher_text = ''
    for letter in text:
        if letter in symbols:
            cipher_text += letter
        else:  # обычная буква
            position = alphabet.index(letter)
            if position + shift > len(alphabet):
                new_position = position + shift - len(alphabet)
            elif position + shift < 0:
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]
    print(cipher_text)

    cipher_text.swapcase()

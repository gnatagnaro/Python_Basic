def vowel(text):
    all_vowel_list = ['а', 'е', 'ё', 'о', 'у', 'э', 'ю', 'я', 'и', 'ы', 'a', 'e', 'i', 'y', 'u', 'o']
    vowel_list = [text[x] for x in range(len(text)) if text[x] in all_vowel_list]

    print(f'Список гласных букв: {vowel_list}')
    print(f'Длина списка: {len(vowel_list)}')


vowel(input('Введите текст: ').lower())

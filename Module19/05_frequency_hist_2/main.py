text = input('Введите текст: ')

text_set = set(text)
word_dict = dict()

for letter in sorted(text_set):
    word_dict[letter] = text.count(letter)

# print(word_dict)

print('Оригинальный словарь частот: ')
for letter in word_dict:
    print('{0} : {1}'.format(letter, word_dict[letter]))

print()

letter_list = []
print('Инвертированный словарь частот: ')
for count in sorted(set(word_dict.values())):
    for letter in word_dict.keys():
        if count == word_dict[letter]:
            letter_list.append(letter)
    print('{0} : {1}'.format(count, letter_list))
    letter_list = []

str_input = input('Введите строку: ').split()

max_len = [len(x) for x in str_input if len(x) > -1]

print('Самое длинное слово: {word}'.format(word=str_input[max_len.index(max(max_len))]))
print('Длина этого слова: {word_len}'.format(word_len=max(max_len)))

import os

zen_file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r', encoding='utf-8').read().lower()
letters = [c for c in zen_file if c.isalpha()]  # можно так if c in 'abcdefghijklmnopqrstuvwxyz'
print('Количество букв в файле: {}'.format(len(letters)),
      'Количество слов в файле: {}'.format(len(zen_file.split())),
      'Количество строк в файле: {}'.format(len(zen_file.splitlines())),  # опять же можно .split('\n')
      'Наиболее редкая буква: {}'.format(min(letters, key=letters.count, default='Нет букв')), sep='\n')

# еще один вариант, но я его забросил на этапе нахождения минимальной буквы по количеству
# zen_file = open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r', encoding='utf-8')
# s = ''
#
# for i in zen_file:
#     s += i
#
# count_alph = 0
# count_n = 0
# minim = 1000
# for j in s:
#     if j == '\n':
#         count_n += 1
#     if j.isalpha():
#         count_alph += 1
#
# zen_file.seek(0)
# x = zen_file.read().split()
# print(x)
#
# print('Количество букв в файле:', count_alph)
# print('Количество слов в файле:', len(x))
# print('Количество строк в файле:', count_n + 1)
# print('Наиболее редкая буква:', )

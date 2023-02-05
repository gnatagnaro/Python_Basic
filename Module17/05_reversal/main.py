text = input('Введите строку: ')

for i in range(len(text)):
    if text[i] == 'h':
        text = text[i + 1:]
        break

minim = 1000000000
for t in range(len(text)):
    if text[t] == 'h' and minim > len(text) - t:
        minim = len(text) - t

for j in range(len(text)):
    if text[j] == 'h' and len(text) - j == minim:
        text = text[:j]
        break

print(f'Развёрнутая последовательность между первым и последним h: {text[::-1]}')

# более короткий вариант решения
# x = input('Введите строку: ')
# first = x.index('h')
# last = x.rindex('h')
#
# print(f'Развёрнутая последовательность между первым и последним h: {x[last-1:first:-1]}')

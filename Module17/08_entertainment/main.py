n = int(input('Количество палок: '))
k = int(input('Количество бросков: '))

enter_str = ['|' for i in range(n)]

for i in range(k):
    print(f'Бросок {i + 1}.\nВведите через запятую с какого по какой номер будут сбиты палки: ', end='')
    left, right = [int(s) for s in input().split(',')]
    for j in range(left - 1, right):
        enter_str[j] = '.'

print('Результат: {0}'.format(''.join(enter_str)))


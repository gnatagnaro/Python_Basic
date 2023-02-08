first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
shift = 0

if first_str == second_str:
    print('Строки одинаковые.')
elif len(first_str) == len(second_str):
    for i in range(len(first_str)-1):
        if first_str == second_str:
            break
        second_str = ''.join([second_str[-1], second_str[:-1]])
        shift += 1


if first_str == second_str:
    print('Первая строка получается из второй со сдвигом {}.'.format(shift))
elif first_str != second_str and len(first_str) == len(second_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print('Строки разной длины.')

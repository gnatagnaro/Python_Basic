print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

size = int(input('Введите число: '))

for line in range(size):
    for left_num in range(size, size - line - 1, -1):
        print(left_num, end='')
    dot_count = 2 * (size - line - 1)
    print('.' * dot_count, end='')
    for right_num in range(size - line, size + 1):
        print(right_num, end='')
    print()
    
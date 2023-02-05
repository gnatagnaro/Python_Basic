import random

count_nums = int(input('Введите количество чисел в списке: '))

before_compression = [random.randint(0, 2) for x in range(count_nums)]
after_compression = [i for i in before_compression if i != 0]

print(f'Список до сжатия: {before_compression}')
print(f'Список после сжатия: {after_compression}')

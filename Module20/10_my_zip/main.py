# все данные вводятся в строку

my_string = input('Строка: ')
nums_tuple = tuple(input('Кортеж чисел: '))
# nums_tuple = (1, 2, 3)
print()

print('Результат:')
x = min(len(my_string), len(nums_tuple))

g = ((my_string[i], int(nums_tuple[i])) for i in range(x))

print(g)
for item in g:
    print(item)


# еще один вариант решения:
# def shortest_sequence_range(*args):
#     return range(len(sorted(args, key=len)[0]))


# g = ((my_string[i], nums_tuple[i]) for i in shortest_sequence_range(my_string, nums_tuple))
# print(g)
# for item in g:
#     print(item)

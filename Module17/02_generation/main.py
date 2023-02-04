len_num_list = int(input('Введите длину списка: '))

generation_list = [1 if i % 2 == 0 else i % 5 for i in range(len_num_list)]

print(f'Результат: {generation_list}')
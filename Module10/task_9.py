print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

count_levels = int(input('Введите количество уровней пирамиды: '))
count = 1

for row in range(count_levels):
    print('\t' * (count_levels - 1 - row), end='')
    for col in range(row + 1):  
        print(count, end='\t\t')
        count += 2
        # print('\t' * 2, end='')
    print()
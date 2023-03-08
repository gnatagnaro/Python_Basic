print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^


size = int(input('Введите размер матрицы: '))

for row in range(size):
    for col in range(size):
        if col == row:
            print('^', end='')
        elif col == size - 1 - row:
            print('^', end='')
        else:
            print(' ', end='')
    print()
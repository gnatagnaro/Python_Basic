print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Питона, 
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.
 
# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?
 
 
# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

def max_3(a, b, c):
    maxim = a
    if b > maxim:
        maxim = b
    if c > maxim:
        maxim = c
    return maxim
    
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
z = float(input('Введите третье число: '))

print(f'Максимальное число из введенных: {max_3(x, y, z)}')
print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def nod(a, b):
    maxim = (a + b + abs(a - b)) // 2
    minim = (a + b - abs(a - b)) // 2

    max_i = 0
    for i in range(1, maxim + 1):
        if minim % i == 0 and maxim % i == 0:
            max_i = i
    print(f'Наибольший общий делитель: {max_i}')

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
nod(x, y)

#еще один способ:
import math

print(f'НОД: {math.gcd(x, y)}')
print('Задача 7. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

num = int(input('Введите четырехзначное число: '))
a = num // 100
b = num // 10
print(num // 1000, a % 10, b % 10, num % 10)
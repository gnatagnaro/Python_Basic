print('Задача 8. Колонтитул')

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку.

x = int(input('Какова общая длина колонтиула в символах? '))
y = int(input('Каково желаемое количество восклицательных знаков? '))

for i in range(True):
    print('~' * ((x - y)//2) + '!' * y + '~' * ((x - y)//2))
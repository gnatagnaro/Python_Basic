import math


def where_is_coin(a, b, c):
    s = math.sqrt(a**2 + b**2)
    if s == c:
        print('Монетка лежит на радиусе')
    elif s < c:
        print('Монетка лежит внутри радиуса')
    else:
        print('Монетка вне радиуса')


print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))

where_is_coin(x, y, r)
print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

x = int(input('Введите сумму вклада в банке в рублях: '))
p = int(input('Введите процент вклада в банке: '))
y = int(input('Введите сумму, до которой должна дойти сумма вклада: '))
z = 0

while True:
    if y >= x:
        years = 0
        while y > x:
            z = int(x * 0.01 * p)
            x += z
            years += 1
        print('Сумма вклада', x, 'дошла до значения', y)
        print('Пройдет', years,
              'лет до того, как сумма вклада X достигнет значения Y')
        break
    else:
        print('Значение Y и так меньше суммы вклада X')
        y = int(input('Введите сумму, до которой должна дойти сумма вклада: '))

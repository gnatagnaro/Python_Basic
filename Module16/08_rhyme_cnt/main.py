def func(a, b):

    out = 0
    for _ in range(len(a) - 1):
        print(f'Текущий круг людей: {a}')
        start = out % len(a)
        print(f'Начало счета с номера: {a[start]}')
        out = (start + b - 1) % len(a)
        print(f'Выбывает человек под номером: {a[out]}')
    print(f'\nОстался человек под номером: {a[0]}')


count_people = list(range(1, int(input('Кол-во человек: ')) + 1))
num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {num}-й человек\n')
func(count_people, num)

def reverse_num(y):
    num = ''
    for i in range(len(y)-1, -1, -1):
        num += y[i]
    return num


def split_num(x):
    s = str(x).split('.')
    a = str(s[0])
    b = str(s[1])
    c = reverse_num(a)
    d = reverse_num(b)
    e = float(c + "." + d)
    if j == 1 or j == 2:
        print(f'{j} число наоборот: {e}')
    else:
        return e


n = float(input('Введите первое вещественное число: '))
m = float(input('Введите второе вещественное число: '))

j = 1
split_num(n)
j += 1
split_num(m)
j += 1
print(f'Сумма: {split_num(n) + split_num(m)}')

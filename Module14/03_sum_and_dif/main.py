def sum_cyph(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

def count_cyph(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input('Введите число: '))
x = sum_cyph(num)
y = count_cyph(num)
print(f'Сумма цифр: {x}')
print(f'Количество цифр: {y}')
print(f'Разность суммы и количества цифр: {x-y}')
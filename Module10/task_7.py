print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input('Введите количество чисел: '))
summ = 0
maxim = 0

for i in range(n):
    print(f'Текущее число №{i + 1}')
    num = int(input('Введите число: '))
    cur_num = num
    while num > 0:
        cur = num % 10
        summ += cur
        num //= 10
    if summ > maxim:
        maxim = summ
        max_sum_num = cur_num
    summ = 0
print(f'Наибольшее число по сумме цифр: {max_sum_num}, а сумма сумма его цифр: {maxim}')
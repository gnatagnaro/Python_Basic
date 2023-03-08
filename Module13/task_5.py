print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def count_num(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count
    

def check_count(a, b, first_n, second_n):   
    if a < 3:
        print("В первом числе меньше трёх цифр.")
        first_n = int(input("Введите первое число: "))
        a = count_num(first_n)
        check_count(a, b, first_n, second_n)    
    else:
        t = func(first_n, a)
        print('Изменённое число:', t)
    if b < 4:
        print("Во втором числе меньше четырёх цифр.")
        second_n = int(input("\nВведите второе число: "))
        b = count_num(second_n)
        check_count(a, b, first_n, second_n)
    else:
        m = func(second_n, b)
        print('Изменённое число:', m)
    print('\nСумма чисел:', t + m)
    print()
    
        
def func(num, len_num):
    last_digit = num % 10
    first_digit = num // 10 ** (len_num - 1)
    between_digits = num % 10 ** (len_num - 1) // 10
    num = last_digit * 10 ** (len_num - 1) + between_digits * 10 + first_digit
    return num 


first_n = int(input("Введите первое число: "))
second_n = int(input("\nВведите второе число: "))
print()
a = count_num(first_n)
b = count_num(second_n)
check_count(a, b, first_n, second_n)
# print('\nСумма чисел:')
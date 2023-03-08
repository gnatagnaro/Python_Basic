print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

x = int(input('Введите число x: '))
temp_up = 1
temp_end = 1
end = 6

for i in range(1, end + 1):
    temp_up *= (x - (2**i - 1)) 
    # print('Верх')
    # print(temp_up)
    # print(f'({x} - {2**i - 1})')

    temp_end *= (x - (2**i))
    # print('Низ')
    # print(temp_end)
    # print(f'({x} - {2**i})')
    # print()

print(f'Значение данного выражения: {temp_up/temp_end}')
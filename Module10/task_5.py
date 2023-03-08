print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

# # start = int(input('Введите начало последовательности: '))
# stop = int(input('Введите конец последовательности: '))
count = 0
size = int(input('Введите кол-во чисел: '))

for i in range(size):
    num = int(input('Введите число: '))
    for divider in range(2, num):
        # print(num, divider)
        if num % divider == 0:
            # print(num, divider)
            break    
    else:
        # print(num)
        count += 1
print(f'Количество простых чисел в последовательности: {count}')


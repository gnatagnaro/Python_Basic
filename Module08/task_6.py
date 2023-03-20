print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

length = int(input('Введите высоту письма: '))
width = int(input('Введите ширину письма: '))
cover_length = 12
cover_width = 12
count_length = 0
count_width = 0

for i in range(True):
    if length > cover_length or width > cover_width:
        while length > cover_length:
            length /= 2
            count_length += 1
        while width > cover_width:
            width /= 2
            count_width += 1
    break
print(f'Письмо нужно сложить пополам по длине {count_length} раз и по ширине {count_width} раз')
print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

size = int(input('Введите высоту пирамиды: '))
count = 1

for row in range(size):
    print(' ' * (size - 1 - row) + '#' * count)
    count += 2
print('Задача 5. Марсоход 2')

# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
# 
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
# 
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
# 
# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

count = int(input('Введите количество шагов: '))
x = 8
y = 10

for i in range(count):
    print(f'[Программа]: Марсоход находится на позиции {x}, {y}, введите команду: ')
    n = input('[Оператор]: ')
    if n == 'W' or n == 'w':
        if y == 20:
            continue
        y += 1
    elif n == 'A' or n == 'a':
        if x == 0:
            continue
        x -= 1
    elif n == 'S' or n == 's':
        if y == 0:
            continue
        y -= 1
    elif n == 'D' or n == 'd':
        if x == 15:
            continue
        x += 1
    else:
        print('Введите команду W, A, S или D')
        i -= 1

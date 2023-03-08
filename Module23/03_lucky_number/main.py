import random

summ = 0
with open('out_file.txt', 'w', encoding='utf-8') as f:
    try:
        while summ < 777:
            cur_num = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                raise Exception
            f.write(str(cur_num) + '\n')
            summ += cur_num
    except Exception:
        print('Вас постигла неудача!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')

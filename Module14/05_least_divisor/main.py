def min_div():
    num = int(input('Введите число: '))
    if num > 1:
        minim = 1000000
        for i in range(2, num + 1):
            if num % i == 0 and i < minim:
                minim = i
        return minim
    else:
        print('Введенное число не больше единицы!')
        print('Наименьший делитель, отличный от единицы:', min_div())


if min_div() != None:
    print('Наименьший делитель, отличный от единицы:', min_div())
print('Задача 1. Космическая еда')

#Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете,
# что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц.
# 
# Чтобы прикинуть гречневый бюджет,
# вы решили написать программу, которая выведет информацию
# о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее,
# пока она не закончится.
# Используйте цикл for.

x = 100
j = 1
for i in range(x, -1, -4):
    if i == 0:
        print('Гречка закончилась :(')
        break
    print(f'На {j} месяц будет в запасе {i} кг гречки')
    j+=1
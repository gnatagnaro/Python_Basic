print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    
    var = random.randint(1, 3)
    x = int(input('Введите число: 1 - если выбираете камень, 2 - ножницы или 3 - бумага": '))
    print()
    
    if x == 1:
        if var == 1:
            print('Ничья!')
        elif var == 2:
            print('Победа!')
        else:
            print('Проигрыш!')
            
    elif x == 2:
        if var == 1:
            print('Проигрыш!')
        elif var == 2:
            print('Ничья!')
        else:
            print('Победа!')
            
    elif x == 3:
        if var == 1:
            print('Победа!')
        elif var == 2:
            print('Проигрыш!')
        else:
            print('Ничья!')
                        
    else:
        print('Вы ввели неправильную команду!')
        rock_paper_scissors()

    next = int(input('Введите 1, если хотите сыграть еще, 2 - если хотите попасть в меню или любую клавишу, если хотите закончить: '))
    print()
    
    if next == 1:
        rock_paper_scissors()
    elif next == 2:
        mainMenu()
    else:
        print('Конец')
        

def guess_the_number():
    #Здесь будет игра "Угадай число"
    start = int(input('Введите начало промежутка: '))
    stop = int(input('Введите конец промежутка: '))
    print()
    var = random.randint(start, stop)

    while True:
        x = int(input('Введите загаданное программой число из промежутка: '))

        if x == var:
            print('Вы угадали!')
            break
        else:
            print('Не верно!')
            print()

    next = int(input('Введите 1, если хотите сыграть еще, 2 - если хотите попасть в меню или любую клавишу, если хотите закончить: '))
    print()
    if next == 1:
        guess_the_number()
    elif next == 2:
        mainMenu()
    else:
        print('Конец')
        
    
def mainMenu():
    #Здесь главное меню игры
    choice = int(input('\n1 - для игры в "Камень, ножницы, бумага";\n2 - для игры в "Угадай число"; \n3 - чтобы закончить. \nВведите число: '))
    print()
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    elif choice == 3:
        print('Конец!')
    else:
        print('Вы ввели неправильную команду!')
        mainMenu()

mainMenu()
contacts = {}


def func():
    print('1. Добавить контакт')
    print('2. Найти человека')
    print('3. Выйти из программы')
    action = input('Введите номер действия: ')

    if action == '1':
        name, surname = input("Введите имя и фамилию нового контакта (через пробел): ").split()
        name_n_surname = (name, surname)
        if name_n_surname not in contacts:
            contacts[name_n_surname] = int(input("Введите номер телефона: "))
        else:
            print("Такой человек уже есть в контактах.")
        print('Текущий словарь контактов:', contacts)
        print()
        func()

    elif action == '2':
        cur_surname = input('Введите фамилию для поиска: ').strip().title()
        print()
        for i, j in contacts.items():
            if cur_surname in i or cur_surname + 'а' in i or cur_surname[:-1] in i:
                print(i[0], i[1], j)
        print()
        func()

    elif action == '3':
        print('До свидания!')

    else:
        print('Вы ввели неправильную команду!')
        print()
        func()


func()

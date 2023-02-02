guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def func():
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    for i in range(len(guests)):
        choice = input('Гость пришел или ушел? ')
        if choice == 'пришел' or choice == 'ушел':
            name = input('Имя гостя: ')
            if choice == 'пришел':
                if len(guests) >= 6:
                    print(f'Прости, {name}, но мест нет.')
                    print()
                    func()
                else:
                    guests.append(name)
                    print(f'Привет, {name}!')
                    print()
                    func()
            elif choice == 'ушел':
                if name in guests:
                    guests.remove(name)
                    print(f'Пока, {name}!')
                    print()
                    func()
                else:
                    print('Данного гостя нет в списке!')
                    print()
                    func()
        elif choice == 'Пора спать':
            print('Вечеринка закончилась, все легли спать.')
            break
        else:
            print('Введена не та команда!')
            print('Если хотите закончить вечеринку, введите "Пора спать".')
            print()
            func()


func()
# MyProfile app

SEPARATOR = '------------------------------------------'

# personal information
n = ''
a = 0
ph = ''
e = ''
index = ''
adress = ''
i = ''
# payment info
OGRNIP = ''
INN = ''
payment_account = ''
bank = ''
BIK = ''
correspondent_account = ''


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, index_parameter, adress_parameter, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19: years_parameter = 'лет'
    elif a_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'


    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', index_parameter)    
    print('Адрес:  ', adress_parameter)
    if i:
            print('')
            print('Дополнительная информация:')
            print(i_parameter)
    

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                        # validate user age
                        a = int(input('Введите возраст: '))
                        if a > 0:
                            break
                        print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch


                e = input('Введите адрес электронной почты: ')
                input_index = input('Введите почтовый индекс: ')
                index = ''
                for i in input_index:
                    if '0' <= i <= '9':
                        index += i
                adress = input('Введите почтовый адрес (без индекса): ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input payment info
                while True:
                    try:
                        OGRNIP = int(input('Введите ОГРНИП: '))
                        if len(str(OGRNIP)) == 15:
                            break
                        else:
                            print('ОГРНИП должен состоять из 15 цифр')
                    except ValueError:
                        print('ОГРНИП должен состоять только из цифр!')
                try:
                    INN = int(input('Введите INN: '))
                except ValueError:
                        print('ИНН должен состоять только из цифр!')    
                while True:
                    try:
                        payment_account = int(input('Введите рассчётный счёт: '))
                        if len(str(payment_account)) == 20:
                            break
                        else:
                            print('Рассчётный счёт должен состоять из 20 цифр')
                    except ValueError:
                        print('Р/с должен состоять только из цифр!')
                bank = input('Введите название банка: ')
                try:
                    BIK = int(input('Введите БИК: '))
                except ValueError:
                        print('БИК должен состоять только из цифр!')
                try:
                    correspondent_account = int(input('Введите корреспондентский счёт: '))
                except ValueError:
                        print('К/с должен состоять только из цифр!')
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, index, adress, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, index, adress, i)

                # print payment info
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП: ', OGRNIP)
                print('ИНН:    ', INN)
                print('Банковские реквизиты')
                print('Р/с:    ', payment_account)
                print('Банк:   ', bank)
                print('БИК:    ', BIK)
                print('К/с:    ', correspondent_account)
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')
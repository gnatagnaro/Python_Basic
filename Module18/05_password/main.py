def register():
    count_upper = 0
    count_digit = 0

    password = input('Придумайте пароль: ')

    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper():
                count_upper += 1
            elif password[i].isdigit():
                count_digit += 1
        if count_upper >= 1 and count_digit >= 3:
            print('Это надёжный пароль!')
        else:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
            register()

    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        register()


register()

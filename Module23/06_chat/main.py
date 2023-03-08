user_name = input('Как вас зовут? ')
while True:
    print('Посмотреть текущий текст чата - 1, отправить сообщение - 2, выход - 3.')
    response = input('Введите 1, 2 или 3: ')
    if response == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('В файле ничего нет\n')
    elif response == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f'{user_name}: {new_message}\n')
    elif response == '3':
        break
    else:
        print('Неизвестная команда\n')

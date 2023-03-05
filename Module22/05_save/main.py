# в задании не написано про ввод диска, поэтому пусть файлы обязательно
# существуют на диске C

import os


def root_path():
    return os.path.abspath(os.sep)


def save():
    text = input('Введите строку: ')
    print()
    save_to = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
    x = os.path.join('C:', os.path.sep, *save_to)
    print()
    if os.path.exists(x):
        my_file = input('Введите имя файла: ') + '.txt'
        my_path = os.path.join(x, my_file)
        if not os.path.exists(my_path):
            my_file_write = open(my_path, 'w', encoding='utf-8')
            my_file_write.write(text)
            my_file_write.close()
            print('\nФайл успешно сохранен!')
        else:
            my_file_write = open(my_path, 'w', encoding='utf-8')
            really = input('Вы действительно хотите перезаписать файл? ').lower()
            if really == 'да':
                my_file_write.write(text)
                my_file_write.close()
                print('\nФайл успешно перезаписан!')
            else:
                print('\nФайл остался без изменений')
    else:
        print('Данного пути не существует')


save()

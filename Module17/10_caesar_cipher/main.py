def caesar_cipher(string, num):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    my_list = [(alphabet[(alphabet.index(i) + num) % len(alphabet)] if i in alphabet else ' ') for i in string]
    my_str = ''
    for j in my_list:
        my_str += j

    return my_str


str_input = input('Введите строку: ').lower()
shift = int(input('Введите сдвиг: '))

print(f'Зашифрованное сообщение: {caesar_cipher(str_input, shift)}')

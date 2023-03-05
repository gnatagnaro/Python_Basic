def caesar_cipher(string, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    my_list = [(alphabet[(alphabet.index(i.lower()) + num) % len(alphabet)]
                if i in alphabet or i in alphabet.upper() else ' ') for i in string]
    my_str = ''

    for count, j in enumerate(my_list):
        if string[count].isupper():
            my_str += j.upper()
        else:
            my_str += j
    return my_str


my_file_1 = open('text.txt', 'r', encoding='utf-8')
my_file_2 = open('cipher_text.txt', 'w', encoding='utf-8')
for shift, i_str in enumerate(my_file_1):
    my_file_2.write(caesar_cipher(i_str, shift + 1) + '\n')
my_file_1.close()
my_file_2.close()

# тоже хороший вариант, но решил не доделывать, так как показалось, что реализация
# сложнее, чем в программе выше

# минус обеих программ в том, что не работают с русским языком
# знаю, как реализовать, добавив в функцию проверку на кириллицу, но, по-моему, это
# не очень красиво, так как код много раз повторяется..

# если кто-то реализовывал программу с русским языком - можно пример, пожалуйста


# def caesar_cipher(string, num):
#     my_str = ''
#     for ch in string:
#         if ch.isalpha():
#             x = ord(ch) + num
#             if x > ord('z'):
#                 x -= 26
#             y = chr(x)
#             my_str += y
#     return my_str
#
#
# shift = 1
# my_file_1 = open('text.txt', 'r', encoding='utf-8')
# my_file_2 = open('cipher_text.txt', 'w', encoding='utf-8')
# for i_str in my_file_1:
#     my_file_2.write(caesar_cipher(i_str, shift) + '\n')
#     shift += 1
# my_file_1.close()
# my_file_2.close()
#

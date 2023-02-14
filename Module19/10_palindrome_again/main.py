def is_palindrom(str):
    char_dict = {}
    for i_sym in str:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


my_string = input('Введите строку: ').lower()

if is_palindrom(my_string):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

# еще один пример
# word = input('Введите строку: ').lower()
# chars = set()
#
# for i in word:
#     if i in chars:
#         chars.remove(i)
#     else:
#         chars.add(i)
# print(('Можно', 'Нельзя')[len(chars) > 1], 'сделать палиндром')

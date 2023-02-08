# еще один вариант, но с конкатенацией

# s = input('Введите строку: ')
# count = 1
# strl = ''
# for i in range(len(s)):
#     if i < len(s)-1 and s[i] == s[i+1]:
#         count += 1
#         # print(count)
#     else:
#         strl += s[i] + str(count)
#         # print('Закончилось')
#         count = 1
#
# print('Закодированная строка: {}'.format(strl))


s = input('Введите строку: ')
count = 1
strl = ''
for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        strl += ''.join([s[i], str(count)])
        count = 1

print('Закодированная строка: {}'.format(strl))

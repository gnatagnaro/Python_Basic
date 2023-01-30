def func(c, d):
    for i in range(a, b + 1):
        x = i // 1000
        y = (i // 100) % 10
        z = (i // 10) % 10
        t = i % 10
        if x == y == z or x == y == t or x == z == t or y == z == t:
            print(i)


a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))

print(f'Годы от {a} до {b} с тремя одинаковыми цифрами: ')
func(a, b)

# еще один вариант решения
# for i in range(a, b + 1):
#     s = str(i)
#     for j in range(0, 1):
#         if s[j] == s[j + 1] == s[j + 2] or s[j] == s[j + 1] == s[j + 3] or s[j] == s[j + 2] == s[j + 3] or s[j + 1] == s[j + 2] == s[j + 3]:
#             print(i)


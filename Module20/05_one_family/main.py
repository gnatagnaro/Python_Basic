d = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Виктор'): 15,
    ('Петрова', 'Дарья'): 16
}

surname = input('Введите фамилию: ').strip().title()
print()

for i, j in d.items():
    if surname in i or surname + 'а' in i or surname[:-1] in i:
        print(i[0], i[1], j)

# еще один вариант:
# family_dict = {
#     ('Сидоров', 'Никита'): 35,
#     ('Сидорова', 'Алина'): 34,
#     ('Сидоров', 'Павел'): 10,
#     ('Петров', 'Виктор'): 15,
#     ('Петрова', 'Дарья'): 16
# }
#
# surname = input('Введите фамилию: ')
#
# if surname.endswith('а'):
#     surname = surname[:-1]
#
# for key, value in family_dict.items():
#     if surname.lower() in key[0].lower():
#         print(key[0], key[1], value)

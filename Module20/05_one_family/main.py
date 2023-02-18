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


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Введите название детали: ')
count_sum = 0
count_name = 0

for i in range(len(shop)):
    if shop[i][0].count(name.lower()) > 0:
        count_name += shop[i][0].count(name.lower())
        count_sum += shop[i][1]

if count_name == 0 and count_sum == 0:
    print('Товар не найден')
else:
    print(f'Кол-во деталей - {count_name}')
    print(f'Общая стоимость - {count_sum}')
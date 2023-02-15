countries_count = int(input('Количество стран: '))
countries = dict()

for country in range(countries_count):
    x = input(f'{country + 1}-ая страна: ').title().split()
    countries[x[0]] = set(x[1:])

for city in range(3):
    y = input(f'{city + 1}-ый город: ').title().split()
    for i in countries.keys():
        if y[0] in countries[i]:
            print(f'Город {y[0]} расположен в стране {i}.')
            break
    else:
        print(f'По городу {y[0]} данных нет.')

# другой вариант
# data_set = {}
# amount_country = int(input('Кол-во стран: '))
#
# for i in range(amount_country):
#     value = input('{} страна: '.format(i + 1)).split()
#     for city in value[1:]:
#         data_set[city] = value[0]
#
# for i in range(3):
#     city = input('\n{} город: '.format(i + 1))
#     country = data_set.get(city)
#     if country:
#         print(f'Город {city} расположен в стране {country}.')
#     else:
#         print(f'По городу {city} данных нет.')

list1 = []
list2 = []

for i in range(3):
    x = int(input(f'Введите {i + 1}-е число для первого списка: '))
    list1.append(x)

for i in range(7):
    x = int(input(f'Введите {i + 1}-е число для первого списка: '))
    list2.append(x)

print(f'\nПервый список: {list1}\n')
print(f'Второй список: {list2}')

list1.extend(list2)

for _ in range(len(list1)):
    for j in list1:
        if list1.count(j) > 1:
            list1.remove(j)

print(f'\nНовый первый список с уникальными элементами: {list1}')

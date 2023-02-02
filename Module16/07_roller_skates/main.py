list_of_skates = []
n = int(input('Кол-во коньков: '))

for i in range(n):
    x = int(input(f'Размер {i + 1}-й пары: '))
    list_of_skates.append(x)

print()

list_of_people = []
k = int(input('Кол-во людей: '))

for i in range(k):
    x = int(input(f'Размер ноги {i + 1}-го человека: '))
    list_of_people.append(x)

maxim = 0
for i in list_of_people:
    for j in list_of_skates:
        # человек может надеть ролики любого размера, которые не меньше размера его ноги
        # поэтому человек с 39 размером ноги сможет надеть ролики 40+ размера (условие задачи)
        if j >= i:
            print(i, '  ', j)
            maxim += 1
            list_of_skates.remove(j)
            break

print(f'Наибольшее кол-во людей, которые могут взять ролики: {maxim}')




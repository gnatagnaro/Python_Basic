list1 = list(range(160, 177, 2))
list2 = list(range(162, 181, 3))
list1.extend(list2)


for i in range(len(list1)):
    for j in range(i, len(list1)):
        if list1[j] < list1[i]:
            list1[j], list1[i] = list1[i], list1[j]

#другой способ: list1.sort()

print(f'Отсортированный список учеников: {list1}')
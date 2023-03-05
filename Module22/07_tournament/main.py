def custom_key(people):
    return people[2]


my_file = open('first_tour.txt', 'r', encoding='utf-8')
my_file_2 = open('second_tour.txt', 'w', encoding='utf-8')

maxim = 0
count = 0
second_list = []
for j, i in enumerate(my_file):
    if j == 0:
        maxim = int(i)
    else:
        my_list = i.split()
        if int(my_list[2]) > maxim:
            my_list[0], my_list[1] = my_list[1][0] + '.', my_list[0]
            second_list.append(my_list)
            count += 1

second_list.sort(key=custom_key, reverse=True)
my_file_2.write(str(len(second_list)) + '\n')
for i, j in enumerate(second_list):
    my_file_2.write(f'{i + 1}) ' + ' '.join(second_list[i]))
    my_file_2.write('\n')

my_file.close()
my_file_2.close()

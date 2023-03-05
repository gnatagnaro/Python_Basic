my_file = open('text.txt', 'r', encoding='utf-8')
my_file_2 = open('analysis.txt', 'w', encoding='utf-8')

my_str = ''.join(my_file.read().lower().split())
my_list = [x for x in my_str if x.isalpha()]
my_dict = dict()
for i, j in enumerate(sorted(my_list)):
    if j not in my_dict:
        my_dict[j] = round(my_list.count(j) / len(my_list), 3)  # my_dict[j] = '{:.3f}'.format(my_list.count(j) / len(my_list))

sorted_dict = dict()
sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = my_dict[w]
    my_file_2.write(w + ' ' + str(sorted_dict[w]) + '\n')

my_file.close()
my_file_2.close()

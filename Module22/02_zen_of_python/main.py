zen_file = open('zen.txt', 'r', encoding='utf-8')
zen_list = zen_file.read().splitlines()  # или можно .split('\n')
print('\n'.join(zen_list[::-1]))

# а еще можно так
# for i_str in zen_file:
#     zen_list.append(i_str)
# for j_str in reversed(zen_list):
#     print(j_str, end='')

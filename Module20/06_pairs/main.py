import random

origin_list = [random.randint(0, 9) for i in range(10)]
new_list = [(j, origin_list[i+1]) for i, j in enumerate(origin_list) if i % 2 == 0]

print('Оригинальный список: {}'.format(origin_list))
print('Новый список: {}'.format(new_list))


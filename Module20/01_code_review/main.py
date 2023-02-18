students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def my_func(my_dict):
    stud_interests = {value for i_key, i_value in students.items() for j_key, j_value in i_value.items() if j_key == 'interests' for index, value in enumerate(j_value)}
    surnames_len = (len(j_value) for i_key, i_value in students.items() for j_key, j_value in i_value.items() if j_key == 'surname')

    sum_len = 0
    for ind, val in enumerate(surnames_len):
        sum_len += val

    return stud_interests, sum_len


id_and_ages = [(i_key, j_value) for i_key, i_value in students.items() for j_key, j_value in i_value.items() if j_key == 'age']
print('Список пар "ID студента — возраст":', id_and_ages)
all_interests, all_len_surname = my_func(students)
print('Полный список интересов всех студентов:', all_interests, '\nОбщая длина всех фамилий студентов:', all_len_surname)

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)
#

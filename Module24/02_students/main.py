class Student:

    def __init__(self, name, group_num, progress):
        self.name = name
        self.group_num = group_num
        self.progress = progress

    def __str__(self):
        res = f'{self.name}, {self.group_num}, {self.average_score()}'
        return res

    def average_score(self):
        return sum(self.progress) / len(self.progress)


students = []
for _ in range(2):
    n = input('Введите имя студента: ')
    gn = input(f'Введите номер группы студента {n}: ')
    p = list(map(int, input(f'Введите успеваемость студента {n} (5 элементов через пробел): ').split()))
    x = Student(n, gn, p)
    students.append(x)
sort = sorted(students, key=lambda student: student.average_score())
print('Отсортированный список студентов по возрастанию среднего балла:\n', *sort, sep='\n')

# была идея реализовать через словари, даже сделал сортировку по значению, но данный
# способ куда сложнее, чем тот, что сверху

# class Student:
#
#     def __init__(self, name, group_num, progress):
#         self.name = name
#         self.group_num = group_num
#         self.progress = progress
#         self.average_score()
#
#     def average_score(self):
#         for key, value in enumerate(self.progress):
#             self.progress[key] = int(value)
#         self.score = sum(self.progress) / len(self.progress)
#
#
# students_dict = {}
# for _ in range(3):
#     n = input('Введите имя студента: ')
#     gn = input(f'Введите номер группы студента {n}: ')
#     p = input(f'Введите успеваемость студента {n} (5 элементов через пробел): ').split()
#     x = Student(n, gn, p)
#     students_dict[(x.name, x.group_num)] = x.score
#
# sorted_dict = dict()
# sorted_keys = sorted(students_dict, key=students_dict.get)
# for i in sorted_keys:
#     sorted_dict[i] = students_dict[i]
# print(sorted_dict)

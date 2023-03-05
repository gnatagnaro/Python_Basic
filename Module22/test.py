# # Задача 1. Сумма чисел
# #
# # Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
# # Напишите программу, которая выводит их сумму в выходной файл answer.txt.
# #
# #
# #
# # Пример:
# #
# # Содержимое файла numbers.txt:
# #
# # 1
# #
# # 2
# #
# # 3
# #
# # 4
# #
# # 10
# #
# #
# #
# # Содержимое файла answer.txt
# #
# # 20
# #
# #
# #
# # import os
#
# # numbers_sum = 0
# # file_from = open("numbers.txt", "r", encoding="utf8")
# # for line in file_from:
# #     clear_line = line.rstrip()
# #     if clear_line:
# #         numbers_sum += int(clear_line)
# # file_from.close()
# #
# # file_in = open("answer.txt", "w", encoding="utf8")
# # file_in.write(str(numbers_sum))
# # file_in.close()
# #
# # nums = 0
# # fl = open('numbers.txt', 'r', encoding='utf-8')
# # for i in fl:
# #     if i:
# #         nums += int(i)
# # fl.close()
# # fl_in = open('answer.txt', 'a', encoding='utf-8')
# # fl_in.write(str(nums) + '\n')
# # fl_in.close()
#
# # Задача 2. Всё в одном
# #
# # Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город,
# # и там у него случилась беда: его диск пришлось отформатировать, а доступ в интернет отсутствует.
# # Остался только телефон с мобильным интернетом. Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом
# # все решения и скрипты, которые у вас сейчас есть.
# #
# #
# #
# # Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic
# # в файл scripts.txt, разделяя код строкой из 40 символов *.
# #
# #
# #
# # Пример содержимого файла scripts.txt:
# #
# # import platform
# #
# # import sys
# #
# #
# #
# # info = 'OS info is \n{}\n\nPython version is {} {}'.format(
# #
# #     platform.uname(),
# #
# #     sys.version,
# #
# #     platform.architecture(),
# #
# # )
# #
# # print(info)
# #
# #
# #
# # with open('os_info.txt', 'w', encoding='utf8') as file:
# #
# #     file.write(info)
# #
# # ****************************************
# #
# # print("Введите первую точку")
# #
# # x1 = float(input('X: '))
# #
# # y1 = float(input('Y: '))
# #
# # print("\nВведите вторую точку")
# #
# # x2 = float(input('X: '))
# #
# # y2 = float(input('Y: '))
# #
# #
# #
# # print("Уравнение прямой, проходящей через эти точки:")
# #
# # x_diff = x1 - x2
# #
# # y_diff = y1 - y2
# #
# # if x_diff == 0:
# #
# #     print("x = ", x1)
# #
# # elif y_diff == 0:
# #
# #     print("y = ", y1)
# #
# # else:
# #
# #     k = y_diff / x_diff
# #
# #     b = y2 - k * x2
# #
# #     print("y = ", k, " * x + ", b)
# #
# # ****************************************
# #
# # …….
# import os
#
#
# def find_file(cur_path, ending):
#     all_paths = []
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if i_elem.endswith(ending):
#             all_paths.append(os.path.abspath(path))
#         elif os.path.isdir(path):
#             result = find_file(path, ending)
#             if result:
#                 all_paths.extend(result)
#
#     return all_paths
#
#
# def get_text_from_file(path_to_file):
#     file = open(path_to_file, "r", encoding="utf8")
#     result = ""
#     for line in file:
#         result += line
#     return result
#
#
# all_py_files = find_file('..', '.py')  # вместо ".." можно вставить путь до папки python_basic
#
# file_result = open("scripts.txt", "w", encoding="utf8")
#
# for file_path in all_py_files:
#     file_result.write(get_text_from_file(file_path))
#     file_result.write("\n" * 2 + "*" * 80 + "\n" * 2)
# file_result.close()
#
#
# # import random
# # import os
# #
# #
# # def find_file(cur_path, file_name):
# #     all_paths = []
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if file_name == i_elem:
# #             all_paths.append(os.path.abspath(path))
# #         elif os.path.isdir(path):
# #             result = find_file(path, file_name)
# #             if result:
# #                 all_paths.extend(result)
# #     return all_paths
# #
# #
# # def check_file_inside(path_to_file):
# #     file = open(path_to_file, 'r', encoding='utf-8')
# #     for line in file:
# #         print(line, end='')
# #     file.close()
# #
# #
# # all_paths = find_file('..', 'main.py')
# # check_file_inside(random.choice(all_paths))
# # import os
# #
# # pth = os.path.join('D:', 'task', 'group_1.txt')
# # pth2 = os.path.join('D:', 'task', 'Additional_info', 'group_2.txt')
# # file = open(pth, 'r', encoding='utf-8')
# # file2 = open(pth2, 'r', encoding='utf-8')
# #
# # summa = 0
# # diff = 0
# # compose = 1
# # for i_line in file:
# #     info = i_line.split()
# #     if info:
# #         summa += int(info[2])
# #         diff -= int(info[2])
# #
# # for i_line in file2:
# #     info = i_line.split()
# #     if info:
# #         compose *= int(info[2])
# # file.close()
# # file2.close()
# # print(summa)
# # print(diff)
# # print(compose)
# #
# # def find_file(cur_path, file_name):
# #     # print('переходим в', cur_path)
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         # print('\t смотрим', path)
# #         if file_name == i_elem:
# #             print(path)
# #         if os.path.isdir(path):
# #             # print('это директория')
# #             res = find_file(path, file_name)
# #             if res:
# #                 break
# #     else:
# #         res = None
# #     return res
# #
# #
# # file_path = find_file(os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic')), 'main.py')
# # if file_path:
# #     print('ABS-path', file_path)
# # else:
# #     print('File not found')
#
# # path = input('Введите путь: ')
# #
# # if os.path.isdir(path):
# #     print('Это директория')
# # elif os.path.isfile(path):
# #     print('Это файл')
# #     print('Размер:', os.path.getsize(path), 'байт')
# # elif os.path.islink(path):
# #     print('Это ссылка')
# # else:
# #     print('Путь не найден')
# # #
# # def find_file(cur_path, file_name):
# #     print('переходим в', cur_path)
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         print('\t смотрим', path)
# #         if file_name == i_elem:
# #             return path
# #         if os.path.isdir(path):
# #             print('это директория')
# #             res = find_file(path, file_name)
# #             if res:
# #                 break
# #     else:
# #         res = None
# #     return res
# #
# #
# # file_path = find_file(os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic')), 'main.py')
# # if file_path:
# #     print('ABS-path', file_path)
# # else:
# #     print('File not found')
#
# # def find_key(struct, key):
# #     if key in struct:
# #         return struct[key]
# #     for sub_struct in struct.values():
# #         if isinstance(sub_struct, dict):
# #             res = find_key(sub_struct, key)
# #             if res:
# #                 break
# #     else:
# #         res = None
# #     return res
#
# # import os.path
# #
# # list_dir = ['Python_Basic', '455', 'basic_collections']
# #
# #
# # def print_dir(my_pth):
# #     print('In: ', my_pth)
# #     if os.path.exists(my_pth):
# #         for i in os.listdir('..'):
# #             print(os.path.join(my_pth, i))
# #     else:
# #         print('Каталога не существует')
# #
# #
# # for dr in list_dir:
# #     pth = os.path.abspath(os.path.join('..', '..', '..', dr))
# #     print_dir(pth)
# #     # print(pth)
#
#
# # import os
# #
# # folder = 'access'
# # file = 'admin.bat'
# # print(os.path.join(folder, file))
# # print(os.path.abspath(os.path.join(folder, file)))
# #
# # print(os.listdir(os.path.abspath(os.path.join('..', '..', '..', 'Python_Basic'))))
# # print(os.listdir('..'))
# # for path in os.listdir(os.path.join('..', '..')):
# #     print(os.path.join(os.path.abspath('..'), path))
# #
# # print(os.path.abspath(os.path.sep))
# # print(os.path.abspath(os.path.join(os.path.sep)))
# # print("Корень диска:", os.path.abspath('.').split(os.path.sep)[0])
# #
# # for path in os.listdir('..'):
# #     print(os.path.join(os.path.abspath('..'), path))
# #
# #
# # for p in os.listdir('..'):
# #     print(os.path.abspath(os.path.join('..', p)))
# #
# #
# # print(os.path.abspath('').split(os.path.sep)[0])
# # print("Корень диска:", os.path.abspath('.').split("\\")[0])

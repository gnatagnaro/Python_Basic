# я придумал так реализовать, но кажется, что есть более логичный способ
# подскажите, пожалуйста, как можно иначе выполнить это задание?

import os

sum_kb = []
count_catalogs = []
count_files = []


def find_file(path):
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            if os.path.isfile(os.path.join(path, i_elem)):  # или так будет правильнее os.path.isfile(i_elem)) ?
                count_files.append(1)
                sum_kb.append(os.path.getsize(os.path.join(path, i_elem)))
            elif os.path.isdir(os.path.join(path, i_elem)):
                count_catalogs.append(1)
                find_file(os.path.join(path, i_elem))
    else:
        return 0
    return sum(sum_kb)/1024, sum(count_catalogs), sum(count_files)


pth = os.path.abspath(os.path.join('..', '..', 'Module14'))
all_paths = find_file(pth)
if all_paths == 0:
    print('Данного пути не существует!')
else:
    print(pth)
    print('Размер каталога (в Кб):', all_paths[0])
    print('Количество подкаталогов:', all_paths[1])
    print('Количество файлов:', all_paths[2])

# import os
#
#
# def calculate_size_and_counts(path):
#     total_size_kb = 0
#     num_subdirs = 0
#     num_files = 0
#
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             total_size_kb += os.path.getsize(file_path) / 1024
#             num_files += 1
#         num_subdirs += len(dirs)
#
#     return (total_size_kb, num_subdirs, num_files)
#
#
# pth = os.path.abspath(os.path.join('..', '..', 'Module14'))
#
# if os.path.exists(pth):
#     all_paths = calculate_size_and_counts(pth)
#     print(pth)
#     print('Размер каталога (в Кб):', all_paths[0])
#     print('Количество подкаталогов:', all_paths[1])
#     print('Количество файлов:', all_paths[2])
# else:
#     print('Данного пути не существует!')

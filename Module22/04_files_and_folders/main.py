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


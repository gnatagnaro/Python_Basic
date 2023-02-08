start_special_symbols = '@ № $ % ^ & * ( )'.split()
end_special_symbols = '.txt .docx'.split()

file_name = input('Введите название файла: ').lower()

for i in range(True):
    if not file_name.endswith(end_special_symbols[i]):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
    elif file_name.startswith(start_special_symbols[i]):
        print('Ошибка: название начинается на один из специальных символов.')
        break
    else:
        print('Файл назван верно.')
        break

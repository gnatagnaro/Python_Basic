start_special_symbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
end_special_symbols = ('.txt', '.docx')

file_name = input('Введите название файла: ').lower()

if file_name.startswith(start_special_symbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith(end_special_symbols):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

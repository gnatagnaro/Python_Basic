try:
    with open('people.txt', 'r', encoding='utf8') as peoples, \
            open('errors.log', 'w', encoding='utf-8') as log_file:
        result = 0
        for count, line in enumerate(peoples):
            try:
                clear_line_len = len(line.rstrip())
                result += clear_line_len
                if clear_line_len < 3:
                    raise Exception(f'Ошибка: менее трёх символов в строке {count}.')
            except (Exception, BaseException) as exc:
                log_file.write(str(exc))
                print(exc)
finally:
    print(f'Общее количество символов: {result}.')

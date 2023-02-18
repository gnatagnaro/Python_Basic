count_records = int(input('Сколько записей вносится в протокол? '))
records_dict = {}

print('Записи (результат и имя): ')
for i_index in range(count_records):
    record, name = input('{0}-я запись: '.format(i_index + 1)).strip().split()
    record = int(record)
    if record > records_dict.get(name, 0):
        if records_dict.get(name, 0):
            records_dict.pop(name)
        records_dict[name] = record

print('\nИтоги соревнований: ')
for i in range(3):
    max_name = ''
    max_record = 0
    for key, value in records_dict.items():
        if value > max_record:
            max_record = value
            max_name = key

    print('{0}-е место. {1} ({2})'.format(i + 1, max_name, max_record))
    if records_dict.get(max_name, 0):
        records_dict.pop(max_name)

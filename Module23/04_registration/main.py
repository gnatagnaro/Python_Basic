def exc_func(line):
    x = line.split()
    if not x:
        raise IndexError('НЕ присутствуют все три поля')
    elif x[0].isalpha() \
            and '@' and '.' in x[1] \
            and 10 <= int(x[2]) <= 99:
        good_log.write(i_line)
    elif not x[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif not ('@' and '.' in x[1]):
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
    elif not (10 <= int(x[2]) <= 99):
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


with open('registrations.txt', 'r', encoding='utf-8') as f, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad_log, \
        open('registrations_good.log', 'w', encoding='utf-8') as good_log:
    for i_line in f:
        try:
            str_file = exc_func(i_line)
        except (NameError, ValueError, SyntaxError, IndexError) as ex:
            bad_log.write(i_line.strip() + '\t\t\t' + str(ex) + '\n')

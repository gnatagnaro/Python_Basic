import collections
import zipfile


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(fl_nm):
    result = {}
    if fl_nm.endswith('.zip'):
        unzip(fl_nm)
        fl_nm = ''.join((fl_nm[:-3], 'txt'))
    text_file = open(fl_nm, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def print_stats(my_dict):
    print('+{:-^9}++{:-^9}+'.format('-', '-'))
    print('|{:^9}||{:^9}|'.format('Буква', 'Частота'))
    print('+{:-^9}++{:-^9}+'.format('-', '-'))
    for i, j in my_dict.items():
        print('|{:^9}||{:^9}|'.format(i, j))
    print('+{:-^9}++{:-^9}+'.format('-', '-'))


def sort_by_frequency(my_dict):
    sorted_dict = collections.OrderedDict()
    sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = my_dict[w]

    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)

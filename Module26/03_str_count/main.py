import os
from collections.abc import Iterable


def str_count(directory: str = os.path.abspath(os.path.join('C:', os.path.sep)), target_dir: str = '') -> Iterable[int]:
    for root, dirs, files in os.walk(directory):
        if target_dir in dirs:
            target_path = os.path.join(root, target_dir)
            for subdir, subdirs, subfiles in os.walk(target_path):
                for file in subfiles:
                    if file.endswith('.py'):
                        file_path = os.path.join(subdir, file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            count = 0
                            for line in lines:
                                if line.strip() and not line.lstrip().startswith('#')\
                                        and not line.lstrip().startswith('"')\
                                        and not line.lstrip().startswith("'"):
                                    #  не знаю, как убрать многострочный комментарий...
                                    #  может быть, в задании учитывались только обычные комментарии?
                                    #  если нет, то подскажите, пожалуйста, как это можно сделать
                                    count += 1
                            yield count

            else:
                return


all_count_lines = 0
for path in str_count(os.path.abspath(os.path.join('C:', os.path.sep)), 'Module25'):
    all_count_lines += path

print(all_count_lines)

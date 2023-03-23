import os
from collections.abc import Iterable


def gen_files_path(directory: str = os.path.abspath(os.path.join('C:', os.path.sep)), target_dir: str = '') -> Iterable[str]:
    for root, dirs, files in os.walk(directory):
        if target_dir in dirs:
            target_path = os.path.join(root, target_dir)
            for subdir, subdirs, subfiles in os.walk(target_path):
                for file in subfiles:
                    file_path = os.path.join(subdir, file)
                    yield file_path
            else:
                return


for path in gen_files_path(os.path.abspath(os.path.join('C:', os.path.sep)), 'Module25'):
    print(path)

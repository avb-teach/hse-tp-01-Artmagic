import sys
import os
import shutil
from collections import defaultdict


# name = sys.argv[0]
input_dir = sys.argv[1]
output_dir = sys.argv[2]

try:
    if sys.argv[3] == "--max_depth":
        max_depth = int(sys.argv[4])
except:
    max_depth = False


try:
    os.mkdir(output_dir)
except FileExistsError:
    pass


def current_depth(indir, current_path):
    current_path.replace(indir, '')
    return current_path.count('\\\\') + 1


duplicates_count = defaultdict()


for info in os.walk(input_dir):
    path = info[0]
    dirs = info[1]
    files = info[2]

    if max_depth and current_depth(input_dir, path) >= max_depth:
        dirs[:] = [] # Позаимствовал, чтобы срез не
        continue #     удалял весь dirs

    for file in files:
        # root_name, extension = file.split('.')

        if duplicates_count[file] == 0:
            name = file
        else:
            name = f'{duplicates_count[file]}{file}'
        duplicates_count[file] += 1

        shutil.copy(path + '\\\\' + file)

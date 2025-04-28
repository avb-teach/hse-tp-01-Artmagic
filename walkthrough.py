import sys
import os
import shutil
from collections import defaultdict

input_dir = sys.argv[1]
output_dir = sys.argv[2]
try:
    max_depth = int(sys.argv[3])
except:
    max_depth = None

try:
    os.mkdir(output_dir)
except FileExistsError:
    pass

duplicates = defaultdict(int)

def current_depth(indir, curr_path):
    curr_path = curr_path.replace(indir, '')
    return curr_path.count('/') + 1


for path, dirs, files in os.walk(input_dir):
    if max_depth is not None and current_depth(input_dir, path) >= max_depth:
        dirs[:] = [] # позаимствовал из интернета, чтобы не удалялся изначальный dirs
        continue

    for file in files:
        count = duplicates[file]
        if count == 0:
            name = file
        else:
            name = f"{count}{file}"
        duplicates[file] += 1

        shutil.copy(path + '/' + file, output_dir + '/' + name)
import sys
import os
import shutil
from collections import defaultdict

input_dir = sys.argv[1]
output_dir = sys.argv[2]

if type(sys.argv) == int:
    max_depth = int(sys.argv[3])
else:
    max_depth = False

os.mkdir(output_dir)


file_counter = defaultdict()

def get_depth(base, path):
    return os.path.relpath(path, base).count(os.sep)

for root, folders, filenames in os.walk(input_dir):
    if max_depth is not None and get_depth(input_dir, root) >= max_depth:
        folders.clear()
        continue

    for filename in filenames:
        source = os.path.join(root, filename)
        name, extension = os.path.splitext(filename)
        idx = file_counter[filename]

        if idx == 0:
            final_name = filename
        else:
            final_name = f"{name}{idx}{extension}"

        file_counter[filename] += 1

        target = os.path.join(output_dir, final_name)
        shutil.copy2(source, target)
import sys
import os
import shutil
from collections import defaultdict

input_dir = sys.argv[1]
output_dir = sys.argv[2]
try:
    max_depth = int(sys.argv[3])
except (IndexError, ValueError):
    max_depth = None

os.makedirs(output_dir, exist_ok=True)

name_counts = defaultdict(int)

def relative_depth(root, path):
    return os.path.relpath(path, root).count(os.sep)

for current_root, dirs, files in os.walk(input_dir):
    if max_depth is not None and relative_depth(input_dir, current_root) >= max_depth:
        dirs[:] = []
        continue

    for file in files:
        full_path = os.path.join(current_root, file)
        base_name, ext = os.path.splitext(file)
        count = name_counts[file]
        if count == 0:
            new_name = file
        else:
            new_name = f"{base_name}{count}{ext}"
        name_counts[file] += 1

        destination = os.path.join(output_dir, new_name)
        shutil.copy2(full_path, destination)

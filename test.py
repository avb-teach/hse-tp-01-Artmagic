import os
import shutil


for info in os.walk("./input_dir"):

    files = info[2]

    for file in files:

        shutil.copy(file, f"./output_dir/{file}")
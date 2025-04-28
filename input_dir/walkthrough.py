import sys
import os

name = sys.argv[0]
input_dir = sys.argv[1]
output_dir = sys.argv[2]

if sys.argv[3] == "--max_depth":
    max_depth = sys.argv[4]
else:
    max_depth = False


try:
    os.mkdir(output_dir)
except FileExistsError:
    pass

for info in os.walk(input_dir):
    path = info[0]
    files = info[2]
    dirs = info[1]

    
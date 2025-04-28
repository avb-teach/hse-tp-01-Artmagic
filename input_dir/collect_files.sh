#!/bin/bash

input_dir="$1"
output_dir="$2"
max_depth=""

if [[ "$3" == "--max_depth" ]]; then
    max_depth="$4"
fi

#if [[ -z "$input_dir" || -z "$output_dir" ]]; then
#    echo "Usage: $0 /path/to/input_dir /path/to/output_dir [--max_depth N]"
#    exit 1
#fi

python3 "$(dirname "$0")/walkthrough.py" "$input_dir" "$output_dir" "$max_depth"
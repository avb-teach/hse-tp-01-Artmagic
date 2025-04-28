#!/bin/bash

input_dir="$1"
output_dir="$2"
max_depth=""

if [[ "$3" == "--max_depth" ]]; then
    max_depth="$4"
fi


python3 "$(dirname "$0")/walkthrough.py" "$input_dir" "$output_dir" "$max_depth"
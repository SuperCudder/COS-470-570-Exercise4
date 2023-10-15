#!/bin/bash

python_script="rmclass.py"
input_file="quotes.tsv"

if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

python3 "$python_script" "$input_file"

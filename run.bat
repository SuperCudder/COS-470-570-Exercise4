@echo off

set python_script=rmclass.py 
set input_file=quotes.tsv

if not exist %input_file% (
    echo Input file "%input_file%" not found.
    exit /b 1
)

python %python_script% %input_file%

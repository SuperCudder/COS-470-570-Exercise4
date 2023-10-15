@echo off

if not exist %input_file% (
    echo Input file "%input_file%" not found.
    exit /b 1
)

python rmclass.py "%~1"

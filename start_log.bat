@echo off

set "flag1="
set "flag2="

if not exist "config.cfg" (
    set "genconf=--genconf"
)

if not exist "text.txt" (
    set "gentext=--gentext"
)

python src/main.py config.cfg text.txt %genconf% %gentext% --log
pause
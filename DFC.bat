@echo off
chcp 65001
setlocal enabledelayedexpansion
set size2=a
set "size2=!size2:a=>!"
:top
mode 60,14
title Dummy-File Creator
cls
set newf=ERR#000#
set /p newf=Enter the name for this file:
if !newf! == ERR#000# goto top
set newf=!newf!.txt
set size=#ERR000#
echo       (SIZE) = (BYTES) / (BITS)      
echo ╔════════════════════════════════════╗
echo ║1 KB = 1024 / 8192                  ║
echo ║1 MB = 1048576 / 8388608            ║
echo ║1 GB = 1073741824 / 8589934592      ║
echo ║1 TB = 1099511627776 / 8796093022208║
echo ║ ENTER "LIST" TO SEE THE SIZE CHART ║
echo ╚════════════════════════════════════╝
echo Enter the amount of bytes to make this file
set /p size=!size2!
if EXIST !newf! del /S /Q /F !newf! >NUL
fsutil file createnew !newf! !size! >NUL
cls
echo  + FINISHED +
timeout 2 >NUL
goto top
@echo off

set ISOFile=..\input\Shinseiki GPX Cyber Formula [J].iso
set GCNISOTargetSize=1459978240
set PS2ISOTargetSize=1239810048

if not exist "%ISOFile%" (
	echo [INFO] "%ISOFile%" was not found
	echo Did you name the ROM correctly and place it in the correct folder?
	echo Exiting in 10 seconds..
	C:\Windows\System32\timeout.exe /t 10 /nobreak >nul
	exit /b 0
)

for %%F in ("%ISOFile%") do (
    set "ISOSize=%%~zF"
)

if %ISOSize% equ %GCNISOTargetSize% (
    echo [INFO] GameCube version detected
    echo [INFO] Compiling patches - Please wait..
    bass\\win\\bass.exe ..\\src\\gcn\\Main.asm
) else if %ISOSize% equ %PS2ISOTargetSize% (
    echo [INFO] PlayStation 2 version detected
    echo [INFO] Compiling patches - Please wait..
    bass\\win\\bass.exe ..\\src\\ps2\\Main.asm
) else (
    echo [INFO] "%ISOFile%" was has an incorrect size
    echo Are you using the uncompressed ROM?
    echo Exiting in 10 seconds..
    C:\Windows\System32\timeout.exe /t 10 /nobreak >nul
    exit /b 0
)

echo [INFO] Patches compiled
echo ---------- 
echo Finished!
echo ----------
C:\Windows\System32\timeout.exe /t 5 /nobreak >nul
exit /b 0
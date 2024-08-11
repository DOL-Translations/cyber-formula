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

set PYTHON_INSTALLED=false
py --version >nul 2>&1
if %errorlevel% == 0 (
    set PYTHON_INSTALLED=true
)

if %ISOSize% equ %GCNISOTargetSize% (
    echo [INFO] GameCube version detected 
    if %PYTHON_INSTALLED% equ true  (
        py "TXTD Repacker.py" ../src/gcn/fs/01_menu.txt ../src/gcn/fs/01_menu.txtd
        py "TXTD Repacker.py" ../src/gcn/fs/02_dialogue.txt ../src/gcn/fs/02_dialogue.txtd
        py "TXTD Repacker.py" ../src/gcn/fs/03_machines.txt ../src/gcn/fs/03_machines.txtd
    ) else (
        echo [INFO] Python is not installed
        echo [INFO] To edit the translation, install Python
    )
    echo [INFO] Compiling patches - Please wait..
    bass\\win\\bass.exe ..\\src\\gcn\\Main.asm
) else if %ISOSize% equ %PS2ISOTargetSize% (
    echo [INFO] PlayStation 2 version detected
    if %PYTHON_INSTALLED% equ true  (
        py "TXTD Repacker.py" ../src/ps2/fs/01_menu.txt ../src/ps2/fs/01_menu.txtd
        py "TXTD Repacker.py" ../src/ps2/fs/02_dialogue.txt ../src/ps2/fs/02_dialogue.txtd
        py "TXTD Repacker.py" ../src/ps2/fs/03_machines.txt ../src/ps2/fs/03_machines.txtd
    ) else (
        echo [INFO] Python is not installed
        echo [INFO] To edit the translation, install Python
    )
    echo [INFO] Compiling patches - Please wait..
    bass\\win\\bass.exe ..\\src\\ps2\\Main.asm
) else (
    echo [INFO] "%ISOFile%" has an incorrect size
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
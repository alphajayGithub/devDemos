@echo off
echo -----------------------------------------------
echo Start to build excelParser
set CURRENT_PATH=%CD%
set TARGET_NAME=excelParser
set PROJECT_ROOT=excelParser
set TARGET_ENTRY=main.py
set VENV_NAME_WIN=devDemos_Win

cd  ..
set ROOT_PATH=%CD%
set BUILD_WIN=%ROOT_PATH%\build_win


echo Do you want to clean %BUILD_WIN%?
RMDIR %BUILD_WIN% /S

if not exist %BUILD_WIN% (
    md  %BUILD_WIN%
)
cd  %BUILD_WIN%

echo target build dir is %BUILD_WIN%
echo ready to build under venv:
pause

move %ROOT_PATH%\%PROJECT_ROOT%\%TARGET_ENTRY% %ROOT_PATH%\%PROJECT_ROOT%\%TARGET_NAME%

call ..\VirtualEnvs\%VENV_NAME_WIN%\Scripts\activate
pyinstaller -F -n %TARGET_NAME%  %ROOT_PATH%\%PROJECT_ROOT%\%TARGET_NAME% --clean
dir dist\*.exe
call ..\VirtualEnvs\%VENV_NAME_WIN%\Scripts\deactivate

move  %ROOT_PATH%\%PROJECT_ROOT%\%TARGET_NAME% %ROOT_PATH%\%PROJECT_ROOT%\%TARGET_ENTRY%
cd    %CURRENT_PATH%
echo -----------------------------------------------
echo build successfully

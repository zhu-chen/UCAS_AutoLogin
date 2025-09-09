@echo off
REM 获取批处理文件所在的目录
set SCRIPT_DIR=%~dp0

REM 使用 pythonw.exe 在后台无窗口运行 Python 脚本
start "AutoLogin" /B pythonw.exe "%SCRIPT_DIR%autologin.py"

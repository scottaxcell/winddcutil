@echo off
@REM
@REM This little utility toggles the input source between HDMI1 and HDMI2 on
@REM a VG27AQ monitor.
@REM

@REM Get the current input source VCP value
@REM Reading command output reference: https://devblogs.microsoft.com/oldnewthing/20120731-00/?p=7003
set WINDDCUTIL=C:\dev\winddcutil\dist\winddcutil.exe
for /f "tokens=1-2, 3" %%i in ('%WINDDCUTIL%  getvcp 1 60') do ^
if "%%i %%j"=="VCP 60" set VCP_VALUE=%%k

@REM Toggle input source VCP value. These values are specific to the VG27AQ monitor.
if %VCP_VALUE%==12 (
	set NEW_VCP_VALUE=11
) else if %VCP_VALUE%==11 (
	set NEW_VCP_VALUE=12
)

@REM Set new input source VCP value.
if defined NEW_VCP_VALUE (
	%WINDDCUTIL% setvcp 1 60 %NEW_VCP_VALUE%
)

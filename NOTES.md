Python 3.11.5 from https://www.python.org/downloads/. Latest version for Windows.

monitorcontrol docs: https://newam.github.io/monitorcontrol/

Environment

```
py -3 -m venv .venv
.venv\Scripts\activate.bat


pip install --upgrade pip setuptools
pip install monitorcontrol
pip install pyinstaller
```

Installer

```
pyinstaller winddcutil.py

dist\winddcutil\winddcutil.exe
```

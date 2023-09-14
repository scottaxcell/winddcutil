# winddcutil

Windows implementation of the [ddcutil](https://github.com/rockowitz/ddcutil) Linux program for querying and changing monitor settings, such as brightness and color levels. Uses the VESA Monitor Control Command Set (MCCS) over the Display Data Channel Command Interface Standard (DDC-CI).

## News

[09-2023] Good news, `winddcutil` has been ported from C++ to Python! We use the API provided by the [monitorcontrol](https://github.com/newAM/monitorcontrol) Python package.

## Usage

The `dist\winddcutil.exe` is a standalone executable that can be run without installing a Python interpreter.

```
usage: winddcutil [-h] {detect,capabilities,setvcp,getvcp} ...

Windows implementation of the ddcutil Linux program for querying and changing monitor settings

positional arguments:
  {detect,capabilities,setvcp,getvcp}
    detect              Detect monitors
    capabilities        Query monitor capabilities
    setvcp              Set VCP feature value
    getvcp              Get VCP feature value

options:
  -h, --help            show this help message and exit
```

## Example application

One useful application of this utility is to toggle between multiple monitor inputs using a keyboard shortcut.

1. Clone this repo to your machine.
2. Copy the `toggle-monitor-input-shortcut.lnk` to the Desktop.
3. Update the Target field in the `toggle-monitor-input-shortcut.lnk` to point to `toggle-monitor-input.bat`.
4. Update the input source VCP values in `toggle-monitor-input.bat:14` for your specific monitor.
5. Update the `WINDDCUTIL` variable in `toggle-monitor-input.bat:9` to point to the `...\winddcutil\dist\winddcutil.exe` on your machine.
6. `Ctrl + Shift + Alt + M` to toggle your monitor input source.

## Development

This Python package is built with Python 3.11.5. Get Python [here](https://www.python.org/downloads/).

### Useful commands

Initialize Python virtual environment

```
py -3 -m venv --upgrade-deps .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

Build standalone distributable [dist\winddcutil.exe]

```
pyinstaller cli.py --name winddcutil --onefile
```

Run tests

```
pytest test
```

Run pre-commit checks on all files

```
pre-commit run --all
```

Bug fixes and enhancement contributions via PRs are welcome!

## License

[MIT License](https://github.com/scottaxcell/winddcutil/blob/main/LICENSE)

## Issues

If you find a bug or have a feature request, please file an issue using [the issue tracker on GitHub](https://github.com/scottaxcell/winddcutil/issues).

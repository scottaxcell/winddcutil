# winddcutil

Windows implementation of the [ddcutil](https://github.com/rockowitz/ddcutil) Linux program for querying and changing monitor settings, such as brightness and color levels. Uses the VESA Monitor Control Command Set (MCCS) over the Display Data Channel Command Interface Standard (DDC-CI).

## News

### Release [2.0.0] - 2023-09-15

- Good news, `winddcutil` has been ported to Python! We use the API provided by the [monitorcontrol](https://github.com/newAM/monitorcontrol) Python package.
- See the [CHANGELOG](https://github.com/scottaxcell/winddcutil/blob/main/CHANGELOG.md) for additional details.

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

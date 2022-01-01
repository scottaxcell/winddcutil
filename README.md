# winddcutil

Windows implementation of the [ddcutil](https://github.com/rockowitz/ddcutil) Linux program for querying and changing monitor settings, such as brightness and color levels.

## Usage

```bat
Usage: winddcutil command [<arg> ...]
Commands:
        help                                           Display help
        detect                                         Detect monitors
        capabilities <display-id>                      Query monitor capabilities
        getvcp <display-id> <feature-code>             Report VCP feature value
        setvcp <display-id> <feature-code> <new-value> Set VCP feature value
```

## Example application

One useful application of this utility is to toggle between multiple monitor inputs using a keyboard shortcut.

1. Clone this repo to your machine.
2. Copy the `toggle-monitor-input-shortcut.lnk` to the Desktop.
3. Update the Target field in the `toggle-monitor-input-shortcut.lnk` to point to `toggle-monitor-input.bat`.
4. Update the input source VCP values in `toggle-monitor-input.bat:14` for your specific monitor.
5. Update the `WINDDCUTIL` variable in `toggle-monitor-input.bat:9` to point to the `...\winddcutil\x64\Release\winddcutil.exe` on your machine.
6. `Ctrl + Shift + Alt + M` to toggle your monitor input source.

## Development

Open `winddcutil.sln` in your favorite flavor of Visual Studio. The original implementation was developed using Visual Studio 2019 Community Edition.

Bug fixes and enhancement contributions via PRs are welcome!

## License

[MIT License](https://github.com/scottaxcell/winddcutil/blob/main/LICENSE)

## Issues

If you find a bug or have a feature request, please file an issue using [the issue tracker on GitHub](https://github.com/scottaxcell/winddcutil/issues).

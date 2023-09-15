# Toggle Monitor Input Source Example

One useful application of this utility is to toggle between multiple monitor inputs using a keyboard shortcut. Below is one method for accomplishing this.

Please add your own example if you have a better method!

1. Clone this repo to your machine.
2. Copy the `toggle-monitor-input-shortcut.lnk` to the Desktop.
3. Update the Target field in the `toggle-monitor-input-shortcut.lnk` to point to `toggle-monitor-input.bat`.
4. Update the input source VCP values in `toggle-monitor-input.bat:14` for your specific monitor.
5. Update the `WINDDCUTIL` variable in `toggle-monitor-input.bat:9` to point to the `...\winddcutil\dist\winddcutil.exe` on your machine.
6. `Ctrl + Shift + Alt + M` to toggle your monitor input source.

"""
          _           _     _            _   _ _
__      _(_)_ __   __| | __| | ___ _   _| |_(_) |
\ \ /\ / / | '_ \ / _` |/ _` |/ __| | | | __| | | Windows implementation of the ddcutil Linux utility
 \ V  V /| | | | | (_| | (_| | (__| |_| | |_| | | https://github.com/scottaxcell/winddcutil
  \_/\_/ |_|_| |_|\__,_|\__,_|\___|\__,_|\__|_|_|

MIT License

Copyright (c) 2020-2023 Scott Axcell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import logging
import sys

from monitorcontrol import get_monitors

logger = logging.getLogger()


def playground() -> None:
    for monitor in get_monitors():
        with monitor:
            print(monitor.get_power_mode())
            caps = monitor.get_vcp_capabilities()
            for k, v in caps.items():
                print(k, " = ", v)

            # monitor.set_power_mode(PowerMode.off_soft)

            # Math conversions
            print("int:", 96, " = hex:", hex(96), " = int:", int("0x60", 16))
            print("0x60" == 0x60)
            print(isinstance(0x60, int))

            # set_vcp_feature can take either the hex or int for a code or value.
            # monitor.vcp.set_vcp_feature(0x60, 0x12)
            # monitor.vcp.set_vcp_feature(96, 18)

            # get_vcp_feature can take either the hex or int for a code or value.
            # print(monitor.vcp.get_vcp_feature(0x60))
            # print(monitor.vcp.get_vcp_feature(96))


def detect(args) -> None:
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            print(i, monitor.vcp.description)
    sys.exit(0)


def capabilities(args) -> None:
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            if i == args.display:
                cap_str = monitor.vcp.get_vcp_capabilities()
                print(cap_str)
                sys.exit(0)

    logger.error("display number did not match any known device ids")
    sys.exit(1)

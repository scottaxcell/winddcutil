import sys
from typing import Callable, Dict

from monitorcontrol import Monitor, get_monitors
from monitorcontrol.vcp import VCPError


def detect(args: Dict[str, str]) -> None:  # pylint: disable=unused-argument
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            print(i, monitor.vcp.description)
    sys.exit(0)


def _capabilities(
    args: Dict[str, str], monitor: Monitor  # pylint: disable=unused-argument
) -> None:
    cap_str = monitor.vcp.get_vcp_capabilities()
    print(cap_str)
    sys.exit(0)


def capabilities(args: Dict[str, str]) -> None:
    _with_monitor(args, _capabilities)


def _set_vcp_feature(args: Dict[str, str], monitor: Monitor) -> None:
    monitor.vcp.set_vcp_feature(args.feature_code, args.new_value)
    sys.exit(0)


def set_vcp_feature(args: Dict[str, str]) -> None:
    _with_monitor(args, _set_vcp_feature)


def _get_vcp_feature(args: Dict[str, str], monitor: Monitor) -> None:
    vcp_code = args.feature_code
    (value, _) = monitor.vcp.get_vcp_feature(vcp_code)
    print(f"VCP {hex(vcp_code)} {value}")
    sys.exit(0)


def get_vcp_feature(args: Dict[str, str]) -> None:
    _with_monitor(args, _get_vcp_feature)


def _with_monitor(
    args: Dict[str, str], handler: Callable[[Dict[str, str], Monitor], None]
) -> None:
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            if i == args.display:
                try:
                    handler(args, monitor)
                except VCPError as e:
                    print(f"ERROR: {e}", file=sys.stderr)
                    sys.exit(1)

    print("ERROR: display id did not match any known device ids", file=sys.stderr)
    sys.exit(1)

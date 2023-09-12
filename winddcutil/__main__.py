"""Main entry point for the winddcutil CLI"""

import argparse
from typing import List, Optional

from . import capabilities, detect, set_vcp_feature


def main(argv: Optional[List[str]] = None):
    parser = get_parser()
    args = parser.parse_args(argv)
    args = args.func(args)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="winddcutil",
        description="Windows implementation of the ddcutil Linux program for querying and changing monitor settings",
    )

    subparsers = parser.add_subparsers()
    parser_detect = subparsers.add_parser("detect", help="Detect monitors")
    parser_detect.set_defaults(func=detect)

    parser_capabilities = subparsers.add_parser(
        "capabilities", help="Query monitor capabilities"
    )
    parser_capabilities.add_argument(
        "display", action="store", type=int, help="Display number"
    )
    parser_capabilities.set_defaults(func=capabilities)

    parser_set_vcp = subparsers.add_parser("setvcp", help="Set VCP feature value")
    parser_set_vcp.add_argument(
        "display", action="store", type=int, help="Display number"
    )
    parser_set_vcp.add_argument(
        "feature_code",
        action="store",
        type=maybe_decimal_or_hex,
        help="Feature code",
    )
    parser_set_vcp.add_argument(
        "new_value", action="store", type=maybe_decimal_or_hex, help="New value"
    )
    parser_set_vcp.set_defaults(func=set_vcp_feature)

    return parser


def maybe_decimal_or_hex(arg: str) -> int:
    try:
        return int(arg)
    except ValueError:
        pass

    try:
        return int(arg, 16)
    except ValueError:
        pass

    raise argparse.ArgumentTypeError(f"invalid decimal or hexidecimal value: '{arg}'")

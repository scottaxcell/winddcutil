import argparse
from typing import List, Optional

from . import capabilities, detect, playground


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

    return parser

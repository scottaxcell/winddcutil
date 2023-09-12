import logging
import sys

from monitorcontrol import get_monitors

logger = logging.getLogger()


def detect(args) -> None:  # pylint: disable=unused-argument
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


def set_vcp_feature(args) -> None:
    for i, monitor in enumerate(get_monitors()):
        with monitor:
            if i == args.display:
                monitor.vcp.set_vcp_feature(args.feature_code, args.new_value)
                sys.exit(0)

    logger.error("display number did not match any known device ids")
    sys.exit(1)

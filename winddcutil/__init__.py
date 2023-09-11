import logging

from .winddcutil import capabilities, detect, set_vcp_feature

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

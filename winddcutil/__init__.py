import logging

from .winddcutil import capabilities, detect, playground

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.ERROR)


#Before  the creating "my_logger.py" check the requirements

import coloredlogs
import logging

logger = logging.getLogger("logger")
coloredlogs.install(level='DEBUG', logger=logger)

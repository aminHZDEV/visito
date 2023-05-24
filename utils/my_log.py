__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import logging
from my_dotenv import MyDotenv


class MyLog(MyDotenv):
    """
    this class is used to config logs
    """

    def __init__(self):
        super().__init__()
        logging.basicConfig(
            filename=self.mdotenv.get("LOG_FILE"),
            filemode=self.mdotenv.get("LOG_MODE"),
            format=self.mdotenv.get("LOG_FORMAT"),
        )
        self._log = logging

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, a):
        self._log = a

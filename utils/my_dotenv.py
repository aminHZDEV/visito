__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import dotenv


class MyDotenv:
    """
    this class is used to dotenv variables
    """

    def __init__(self):
        self._mdotenv = dotenv.dotenv_values()

    @property
    def mdotenv(self):
        return self._mdotenv

    @mdotenv.setter
    def mdotenv(self, a):
        self._mdotenv = a

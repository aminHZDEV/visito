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
        self._dotenv_values = dotenv.dotenv_values()

    @property
    def dotenv_values(self):
        return self._dotenv_values

    @dotenv_values.setter
    def dotenv_values(self, a):
        self._dotenv_values = a

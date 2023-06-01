__author__ = "hamedheidarian"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv

de = MyDotenv()


class Service:
    def __init__(
        self,
        name,
        price,
        duration
    ):
        self._name = name
        self._price = price
        self._duration = duration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, a):
        self._price = a

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, a):
        self._duration = a
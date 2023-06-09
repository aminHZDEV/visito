__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

import datetime

from app.model.doctor import Doctor
from app.model.patient import Patient


class Medicine:
    def __init__(self, name: str = "", quantity: int = 0, id_cart=None):
        self._name = name
        self._quantity = quantity
        self._id_cart = id_cart

    # Setters and Getters lie beyond this comment
    # name accessor
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    # Quantity accessor
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, a):
        self._quantity = a

    # ID accessor
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    def increase_quantity(self, amount: int = 1):
        self.quantity += amount

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Medicine
        :return: A dummy Medicine object
        """
        return Medicine('Dummy Drug', 50)

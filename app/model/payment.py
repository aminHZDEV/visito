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


class Payment:
    def __init__(self, amount: int = -1, invoice_number: str = "", date: str = "1990-01-01 01:00 AM", id_cart=None):
        self._amount = amount
        self._invoice_number = invoice_number
        self._date = datetime.datetime.strptime(date, "%Y-%m-%d %I:%M %p")
        self._id_cart = id_cart

    # Setters and Getters lie beyond this comment
    # Amount Accessor
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, a):
        self._amount = a

    # Invoice ID accessor
    @property
    def invoice_number(self):
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, a):
        self._invoice_number = a

    # ID accessor
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    # Date accessor
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, a):
        self._date = datetime.datetime.strptime(a, "%Y-%m-%d %I:%M %p")

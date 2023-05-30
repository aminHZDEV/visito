__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"


class Doctor:
    def __init__(self, name: str = "", gmc_number: str = "", field: str = "", id_cart=None):
        self._name = name
        self._gmc_number = gmc_number
        self._field = field
        self._id_cart = id_cart

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    @property
    def gmc_number(self):
        return self._gmc_number

    @gmc_number.setter
    def gmc_number(self, a):
        self._gmc_number = a

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, a):
        self._field = a

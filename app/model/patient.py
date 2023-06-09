__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"


class Patient:
    def __init__(self, name: str = "", ssid: str = "", id_cart: int = -1):
        self._name = name
        self._ssid = ssid
        self._id_cart = id_cart

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def ssid(self):
        return self._ssid

    @ssid.setter
    def ssid(self, a):
        self._ssid = a

    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Patient
        :return: A dummy Patient object
        """
        return Patient('Default Pearson', 'xxxxxxxxxx')

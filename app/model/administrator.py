__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "mehdiroudaki@hotmail.com"
__status__ = "Production"


class Administrator:
    def __init__(self, name: str = "", username: str = "", password: str = "", id_cart=None):
        self._name = name
        self._id_cart = id_cart
        self._username = username
        self._password = password

    # Setters and Getters lie beyond this comment
    # Name accessors
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    # ID accessors
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    # Username accessors
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, a):
        self._username = a

    # Password accessors
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, a):
        self._password = a

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Administrator
        :return: A dummy Administrator object
        """
        return Administrator('Default Pearson', 'dummy', 'dummy')

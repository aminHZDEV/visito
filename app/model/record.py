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


class Record:
    def __init__(self, patient: Patient = None, token: str = "", info: str = "", date: str = "1990-01-01 01:00 AM",
                 id_cart=None):
        self._patient = patient
        self._token = token
        self._info = info
        self._date = datetime.datetime.strptime(date, "%Y-%m-%d %I:%M %p")
        self._id_cart = id_cart

    # Setters and Getters lie beyond this comment
    # Patient Accessor
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, a):
        self._patient = a

    # Token accessor
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, a):
        self._token = a

    # Info accessor
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, a):
        self._info = a

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

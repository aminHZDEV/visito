__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "mehdiroudaki@hotmail.com"
__status__ = "Production"

from app.model.patient import Patient
from app.model.doctor import Doctor


class Appointment:
    def __init__(self, patient: Patient = None, doctor: Doctor = None, date: str = "", id_cart=None):
        self._patient = patient
        self._doctor = doctor
        self._date = date
        self._id_cart = id_cart

    # Setters and Getters lie beyond this comment
    # Patient Accessor
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, a):
        self._patient = a

    # Doctor Accessor
    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, a):
        self._doctor = a

    # Date accessor
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, a):
        self._date = a

    # ID accessor
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

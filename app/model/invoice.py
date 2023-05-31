__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

from app.model.patient import Patient
from app.model.payment import Payment


class Invoice:
    def __init__(self, patient: Patient = None, service: str = "",
                 amount: int = -1, invoice_number: str = "",
                 payments: list = None, id_cart=None):
        self._patient = patient
        self._service = service
        self._amount = amount
        self._invoice_number = invoice_number
        if payments is None:
            self._payments = []
        else:
            self._payments = payments
        self._id_cart = id_cart

    # Setters and Getters lie beyond this comment
    # Patient Accessor
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, a):
        self._patient = a

    # Service Accessor
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, a):
        self._service = a

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

    # Payments accessor
    @property
    def payments(self):
        return self._payments

    @payments.setter
    def payments(self, a):
        self._payments = a

    # ID accessor
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    # Class methods
    def add_payment(self, payment: Payment) -> bool:
        try:
            self.payments.append(payment)
            return True
        except:
            return False

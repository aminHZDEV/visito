__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

from app.db.base import Base
from app.model.patient import Patient
from app.model.payment import Payment
from utils.status import InsertStatus, FindStatus


class Invoice(Base):
    def __init__(self, patient: Patient = None, service: str = "", amount: int = -1, invoice_number: str = "",
                 payments: list = None, id_cart=None):
        super().__init__()
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
        """
        Adds the given payment information to this invoice
        :param payment: A Payment record meant for this invoice
        :return: True if operation was successful and False if it fails
        """
        try:
            self.payments.append(payment)
            return True
        except Exception as e:
            print(f'Something bad happened while we were trying to add payment. Exception:\n{e}')
            return False

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                if self._invoice_number == "":
                    self.log.error('Insufficient info was given for invoice lookup')
                    return FindStatus.INSUFFICIENT_INFO
                record = collection.find_one({'invoice_number': self._invoice_number})
                if record:
                    self._id_cart = record['_id']
                    patient = Patient(id_cart=record['patient_id'])
                    patient.find_and_update()
                    self._patient = patient
                    self._service = record['service']
                    self._amount = record['amount']
                    self._payments = record['payments']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn(f'No records found for invoice number {self._invoice_number}.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    patient = Patient(id_cart=record['patient_id'])
                    patient.find_and_update()
                    self._patient = patient
                    self._service = record['service']
                    self._amount = record['amount']
                    self._invoice_number = record['invoice_number']
                    self._payments = record['payments']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn(f'No records found for id: {self._id_cart}')
                    return FindStatus.NO_RECORDS
        except Exception as e:
            self.log.error(f'Unexpected exception:\n\t{e}')
            return FindStatus.UNEXPECTED_ERROR

    def add(self, update: bool = False) -> InsertStatus:
        """
        Updates the entry or adds this object to base database
        :param update: If it's True updates the database entry if it already exists
        :return: Returns a InsertInsert type enum
        """
        if self._patient is None or self._invoice_number == "" or self._amount < 0 or self._service == "":
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'invoice_number': self._invoice_number})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'payments': self._payments}})
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn('An identical appointment already exists')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'patient_id': self._patient.id_cart,
                                                    'service': self._service,
                                                    'amount': self._amount,
                                                    'payments': self._payments,
                                                    'invoice_number': self._invoice_number})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'patient_id': self._patient.id_cart,
                                                                                'service': self._service,
                                                                                'amount': self._amount,
                                                                                'payments': self._payments,
                                                                                'invoice_number': self._invoice_number}
                                                                       })
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn('This entry was inserted before. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ID
                else:
                    self.log.error('Weird ID was provided. ID must be either a valid ID or None.'
                                   f'Your ID: {self._id_cart}')
                    return InsertStatus.BAD_ID
        except Exception as e:
            self.log.error(f'Unexpected exception:\n\t{e}')
            return InsertStatus.UNEXPECTED_ERROR

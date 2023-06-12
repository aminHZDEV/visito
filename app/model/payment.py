__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

import datetime

from app.db.base import Base
from app.model.doctor import Doctor
from app.model.patient import Patient
from utils.status import InsertStatus, FindStatus


class Payment(Base):
    def __init__(self, amount: int = -1, invoice_number: str = "", date: str = "1990-01-01 01:00 AM", id_cart=None):
        super().__init__()
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

    # Comparison overload
    def __eq__(self, other):
        if self._id_cart is None:
            raise AttributeError('Get the ID first!')
        return self._id_cart == other._id_cart

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self._id_cart)

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Payment
        :return: A dummy Payment object
        """
        return Payment(50, 'INV-0000', '1990-01-01 01:00 AM')

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                if self._invoice_number == "" or self._amount == -1:
                    self.log.error('Insufficient info was given for payment lookup')
                    return FindStatus.INSUFFICIENT_INFO
                record = collection.find_one({'amount': self._amount,
                                              'invoice_number': self._invoice_number,
                                              'date': self._date})
                if record:
                    self._id_cart = record['_id']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn('No records found for queried payment.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    self._amount = record['amount']
                    self._invoice_number = record['invoice_number']
                    self._date = record['date']
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
        if self._invoice_number == "" or self._amount == -1:
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'amount': self._amount,
                                              'invoice_number': self._invoice_number,
                                              'date': self._date})
                if record:
                    self._id_cart = record['_id']
                    if update:
                        self.log.error('Updating entry based on that many information is not allowed!'
                                       ' Please use ID based update.')
                        return InsertStatus.UPDATE_NOT_ALLOWED
                    else:
                        self.log.warn('An identical appointment already exists')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'amount': self._amount,
                                                    'invoice_number': self._invoice_number,
                                                    'date': self._date})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'amount': self._amount,
                                                                                'invoice_number': self._invoice_number,
                                                                                'date': self._date}})
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

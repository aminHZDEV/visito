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
from app.model.patient import Patient
from utils.status import InsertStatus, FindStatus


class Record(Base):
    def __init__(self, patient: Patient = None, token: str = "", info: str = "", date: str = "1990-01-01 01:00 AM",
                 id_cart=None):
        super().__init__()
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

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                if self._token == "":
                    self.log.error('Insufficient info was given for record lookup')
                    return FindStatus.INSUFFICIENT_INFO
                record = collection.find_one({'token': self._token})
                if record:
                    patient = Patient(id_cart=record['patient_id'])
                    patient.find_and_update()
                    self._patient = patient
                    self._info = record['info']
                    self._date = record['date']
                    self._id_cart = record['_id']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn(f'No records found for token {self._token}.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    patient = Patient(id_cart=record['patient_id'])
                    patient.find_and_update()
                    self._patient = patient
                    self._info = record['info']
                    self._date = record['date']
                    self._token = record['token']
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
        if not (self._patient and self._token and self._info):
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'token': self._token})
                if record:
                    self._id_cart = record['_id']
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'info': self._info}})
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn(f'An entry for token {self._token} already exists. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'patient_id': self._patient.id_cart,
                                                    'token': self._token,
                                                    'info': self._info,
                                                    'date': self._date})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'patient_id': self._patient.id_cart,
                                                                                'token': self._token,
                                                                                'info': self._info,
                                                                                'date': self._date}
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

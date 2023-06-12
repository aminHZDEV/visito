__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "mehdiroudaki@hotmail.com"
__status__ = "Production"

import datetime

from app.model.doctor import Doctor
from app.model.patient import Patient
from utils.status import FindStatus, InsertStatus
from app.db.base import Base


class Appointment(Base):
    def __init__(self, patient: Patient = None, doctor: Doctor = None, date: str = "1990-01-01 01:00 AM", id_cart=None):
        super().__init__()
        self._patient = patient
        self._doctor = doctor
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
        self._date = datetime.datetime.strptime(a, "%Y-%m-%d %I:%M %p")

    # ID accessor
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                if self._patient is None or self._doctor is None:
                    self.log.error('Insufficient info was given for appointment lookup')
                    return FindStatus.INSUFFICIENT_INFO
                record = collection.find_one({'patient_id': self._patient.id_cart,
                                              'doctor_id': self._doctor.id_cart,
                                              'date': self._date})
                if record:
                    self._id_cart = record['_id']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn('No records found for queried appointment.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    patient = Patient(id_cart=record['patient_id'])
                    patient.find_and_update()
                    self._patient = patient
                    doctor = Doctor(id_cart=record['doctor_id'])
                    doctor.find_and_update()
                    self._doctor = doctor
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
        if self._doctor is None or self._patient is None:
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'patient_id': self._patient.id_cart,
                                              'doctor_id': self._doctor.id_cart,
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
                    record = collection.insert_one({'patient_id': self._patient.id_cart,
                                                    'doctor_id': self._doctor.id_cart,
                                                    'date': self._date})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'patient_id': self._patient.id_cart,
                                                                                'doctor_id': self._doctor.id_cart,
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

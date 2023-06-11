__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from app.db.base import Base
from utils.status import InsertStatus, FindStatus


class Doctor(Base):
    def __init__(self, name: str = "", gmc_number: str = "", field: str = "", id_cart=None):
        super().__init__()
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

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Doctor
        :return: A dummy Doctor object
        """
        return Doctor('Default Pearson', 'xxxxxxx', 'dummiologist')

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'gmc_number': self._gmc_number})
                if record:
                    self._id_cart = record['_id']
                    self._name = record['name']
                    self._field = record['field']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.warn(f'No records found for doctor {self._gmc_number}.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    self._name = record['name']
                    self._field = record['field']
                    self._gmc_number = record['gmc_number']
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
        if not (self._field and self._name and self._gmc_number):
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'gmc_number': self._gmc_number})
                if record:
                    self._id_cart = record['_id']
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                                'field': self._field}})
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn(f'An entry for GMC number {self._gmc_number} already exists. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'name': self._name,
                                                    'gmc_number': self._gmc_number,
                                                    'field': self._field})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                                'gmc_number': self._gmc_number,
                                                                                'field': self._field}
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

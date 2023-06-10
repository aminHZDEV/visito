__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"


from app.db.base import Base
from utils.status import FindStatus, InsertStatus


class Patient(Base):
    def __init__(self, name: str = "", ssid: str = "", id_cart: int = -1):
        super().__init__()
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

    # A wild static method appears
    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Patient
        :return: A dummy Patient object
        """
        return Patient('Default Pearson', 'xxxxxxxxxx')

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__name__]
            if self.id_cart == -1:
                record = collection.find_one({'name': self._name, 'ssid': self._ssid})
                if record:
                    self._id_cart = record['_id']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.error(f'No records found for patient {self._name}, {self._ssid}')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    self._name = record['name']
                    self._ssid = record['ssid']
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
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__name__]
            if self.id_cart == -1:
                record = collection.find_one({'ssid': self._ssid})
                if record:
                    self._id_cart = record['_id']
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name}})
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn(f'An entry for ssid {self._ssid} already exists. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'name': self._name, 'ssid': self._ssid})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                                'ssid': self._ssid}
                                                                       })
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn('This entry was inserted before. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ID
                else:
                    self.log.error('Weird ID was provided. ID must be either a valid ID or -1')
                    return InsertStatus.BAD_ID
        except Exception as e:
            self.log.warn(f'Unexpected exception:\n\t{e}')
            return InsertStatus.UNEXPECTED_ERROR

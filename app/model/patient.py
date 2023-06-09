__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"


from pymongo.database import Database

class Patient:
    def __init__(self, name: str = "", ssid: str = "", id_cart: int = -1):
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
    def find_and_update(self, database: Database) -> int:
        """
        Searches the given database and update this object
        :param database: Target Database
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        collection = database[self.__name__]
        if self.id_cart is -1:
            record = collection.find_one({'name': self._name, 'ssid': self._ssid})
            if record:
                self._id_cart = record['_id']
                return 1   # Successfully found
            else:
                return -1  # No records found
        else:
            record = collection.find_one({'_id': self._id_cart})
            if record:
                self._name = record['name']
                self._ssid = record['ssid']
                return 1   # Successfully found
            else:
                return -1  # No records found

    def add(self, database: Database, update: bool = False) -> int:
        """
        Updates the entry or adds this object to given database
        :param update: If it's True updates the database entry if it already exists
        :param database: Target Database
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        collection = database[self.__name__]
        if self.id_cart is -1:
            record = collection.find_one({'ssid': self._ssid})
            if record:
                if update:
                    self._id_cart = record['_id']
                    collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name}})
                    return 2   # Updated successfully
                else:
                    return -2  # Duplicate entry error
            else:
                record = collection.insert_one({'name': self._name, 'ssid': self._ssid})
                self._id_cart = record.inserted_id
                return 1  # Inserted successfully
        else:
            record = collection.find_one({'_id': self._id_cart})
            if record:
                if update:
                    collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                            'ssid': self._ssid}
                                                                   })
                    return 2   # Updated successfully
                else:
                    return -2  # Duplicate entry error
            else:
                return -3  # Bad ID

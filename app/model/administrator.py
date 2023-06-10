__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "mehdiroudaki@hotmail.com"
__status__ = "Production"


from app.db.base import Base
from utils.status import FindStatus, InsertStatus


class Administrator(Base):
    def __init__(self, name: str = "", username: str = "", password: str = "", id_cart=None):
        super().__init__()
        self._name = name
        self._id_cart = id_cart
        self._username = username
        self._password = password

    # Setters and Getters lie beyond this comment
    # Name accessors
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    # ID accessors
    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a

    # Username accessors
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, a):
        self._username = a

    # Password accessors
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, a):
        self._password = a

    @staticmethod
    def make_dummy():
        """
        Create a dummy object for testing purposes
        :rtype: Administrator
        :return: A dummy Administrator object
        """
        return Administrator('Default Pearson', 'dummy', 'dummy')

    # Database operations rest in this place
    def find_and_update(self) -> FindStatus:
        """
        Searches the base database and update this object
        :return: Returns 1 if operation was successful and -1 if it doesn't find the record
        """
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'username': self._username})
                if record:
                    self._id_cart = record['_id']
                    self._name = record['name']
                    self._password = record['password']
                    return FindStatus.RECORD_FOUND
                else:
                    self.log.error(f'No records found for administrator {self._username}.')
                    return FindStatus.NO_RECORDS
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    self._name = record['name']
                    self._username = record['username']
                    self._password = record['password']
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
        if not (self._username and self._name and self._password):
            self.log.error('Incomplete information! Please first fill the object.')
            return InsertStatus.INCOMPLETE_INFO
        try:
            collection = self.my_db[self.__class__.__name__]
            if self.id_cart is None:
                record = collection.find_one({'username': self._username})
                if record:
                    self._id_cart = record['_id']
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                                'password': self._password}})
                        return InsertStatus.UPDATED_SUCCESSFULLY
                    else:
                        self.log.warn(f'An entry for username {self._username} already exists. '
                                      'Set the update flag if you want to update it!')
                        return InsertStatus.DUPLICATE_ENTRY
                else:
                    record = collection.insert_one({'name': self._name,
                                                    'username': self._username,
                                                    'password': self._password})
                    self._id_cart = record.inserted_id
                    return InsertStatus.INSERTED_SUCCESSFULLY
            else:
                record = collection.find_one({'_id': self._id_cart})
                if record:
                    if update:
                        collection.update_one({'_id': self._id_cart}, {'$set': {'name': self._name,
                                                                                'username': self._username,
                                                                                'password': self._password}
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

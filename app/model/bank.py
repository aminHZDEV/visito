__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from app.db.base import Base


class Bank(Base):
    def __init__(self, name: str = "", email: str = "", number: str = ""):
        super().__init__()
        self._name = name
        self._email = email
        self._number = number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, a):
        self._email = a

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, a):
        self._number = a

    def send(self, entity: object = None, message: str = "") -> bool:
        try:
            entity.send(message=message)
            return True
        except Exception as e:
            self.log.info(e)
            return False

    def add(self) -> int:
        """
        this method add patient model to database
        :return:
        """
        try:
            record = self.my_db[Bank.__name__].insert_one(
                {"name": self.name, "email": self.email, "number": self.number}
            )
            self.id_cart = record.inserted_id
            return self.id_cart
        except Exception as e:
            self.log.error(e)
            return -1

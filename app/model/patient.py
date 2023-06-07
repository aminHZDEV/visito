__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from app.db.base import Base


class Patient(Base):
    def __init__(self, name: str = "", id_cart: int = -1):
        super().__init__()
        self._name = name
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

    def add(self) -> int:
        """
        this method add patient model to database
        :return:
        """
        try:
            record = self.my_db[Patient.__name__].insert_one(
                {
                    "name": self.name,
                }
            )
            self.id_cart = record.inserted_id
            return self.id_cart
        except Exception as e:
            self.log.error(e)
            return -1

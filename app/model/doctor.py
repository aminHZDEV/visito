__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from app.model.user import User


class Doctor(User):
    def __init__(self, name: str = "", id_cart: int = -1):
        super().__init__(name=name, id_cart=id_cart)

    def add(self) -> int:
        """
        this method add doctor model to database
        :return:
        """
        try:
            record = self.my_db[Doctor.__name__].insert_one(
                {
                    "name": self.name,
                }
            )
            self.id_cart = record.inserted_id
            return self.id_cart
        except Exception as e:
            self.log.error(e)
            return -1

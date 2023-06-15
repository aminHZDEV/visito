__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from app.db.base import Base


class Patient(Base):

    def __init__(
        self,
        name: str = "",
        id_cart: int = -1,
        reason: str = "",
        payment_method: str = "",
        phonenumber: str = "",
        email: str = "",
        height: int = -1,
        weight: int = -1
    ):
        super().__init__()
        self._name = name
        self._id_cart = id_cart
        self._reason = reason
        self._payment_method = payment_method
        self._phonenumber = phonenumber
        self._email = email


        self._height = height
        self._weight = weight

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
    def phonenumber(self):
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, a):
        self._phonenumber = a

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, a):
        self._reason = a

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, a):
        self._payment_method = a

    @property
    def id_cart(self):
        return self._id_cart

    @id_cart.setter
    def id_cart(self, a):
        self._id_cart = a


    def send(self, entity: object = None, message: str = "") -> bool:
        """
        this method is used to send confirmation to patient
        :param entity:
        :param message:
        :return:
        """
        try:
            entity.send(message=message)
            return True
        except Exception as e:
            self.log.error(e)
            return False

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, a):
        self.height = a


    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, a):
        self.weight = a


    def add(self) -> int:
        """
        this method add patient model to database
        :return:
        """
        try:
            record = self.my_db[Patient.__name__].insert_one(
                {
                    "name": self.name,
                    "reason": self.reason,
                    "payment_method": self.payment_method,
                    "phone_number": self.phonenumber,
                    "email": self.email,
                }
            )
            self.id_cart = record.inserted_id
            return self.id_cart
        except Exception as e:
            self.log.error(e)
            return -1
    def update_height_weight(self , patient_id , hight , weight) -> bool:
        """
        this method add patient model to database
        :return:
        """
        try:
            record = self.my_db[Patient.__name__].update_one({"_id_cart": patient_id} ,{"$set":{"height":hight , "weight":weight}} )

            return True
        except Exception as e:
            print("error in updating height and weight")
            self.log.error(e)
            return False

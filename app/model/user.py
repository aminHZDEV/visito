from abc import ABC, abstractmethod
from app.db.base import Base


class User(ABC, Base):
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

    @abstractmethod
    def add(self):
        raise NotImplementedError

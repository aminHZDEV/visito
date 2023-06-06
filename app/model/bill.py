__author__ = "Taravat"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tarvtm@gmail.com"
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv
from app.db.base import Base
de = MyDotenv()


class Bill(Base):
    def __init__(
        self,
        bill_id: int = -1,
        duration=-1,
        amount=-1,
    ):
        super().__init__()
        self._bill_id = bill_id
        self._duration = duration
        self._amount = amount

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, a):
        self._bill_id = a

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def doctor_id(self, a):
        self._duration = a

    @property
    def amount(self):
        return self.amount

    @amount.setter
    def amount(self, a):
        self._amount = a
    def add(self) -> int:
        """
        this method add patient model to database
        :return:
        """
        try:
            record = self.my_db[Bill.__name__].insert_one({})
            self.bill_id = record.inserted_id
            return self.bill_id
        except Exception as e:
            self.log.error(e)
            return -1


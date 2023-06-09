__author__ = "hamedheidarian"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv

de = MyDotenv()


class Appointment:
    def __init__(
        self,
        name,
        date,
        time
    ):
        self._name = name
        self._date = date
        self._time = time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, a):
        self._date = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

        def add(self) -> int:
            """
            this method add appointment model to database
            :return:
            """
            try:
                record = self.my_db[Appointment.__name__].insert_one(
                    {
                        "date": self.date,
                        "name": self.name,
                        "time": self.time,
                    }
                )
                return record
            except Exception as e:
                self.log.error(e)
                return -1
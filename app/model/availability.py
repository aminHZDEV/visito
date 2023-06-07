__author__ = "isaac1998sm"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "isaacsalmanpour@gmail.com"
__status__ = "Production"

from datetime import time
from app.db.base import Base


class Availability(Base):

    def __init__(self, start, end, date):
        super().__init__()
        self._start = start
        self._end = end
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end



    def add(self) -> int:
        """
        this method add doctor model to database
        :return:
        """
        try:
            record = self.my_db[Availability.__name__].insert_one(
                {
                    "date": self.date,
                    "start": self.start,
                    "end": self.end,
                }
            )
            return record
        except Exception as e:
            self.log.error(e)
            return -1


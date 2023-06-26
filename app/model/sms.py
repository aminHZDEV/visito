from app.model.confirmation import Confirmation
from utils.my_log import MyLog


class SMS(MyLog, Confirmation):
    def __init__(self, number):
        super().__init__()
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, a):
        self._number = a

    def send(self, message):
        self.log.info(f"send sms : {message} to {self.number} address")

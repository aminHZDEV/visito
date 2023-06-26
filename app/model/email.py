from app.model.confirmation import Confirmation
from utils.my_log import MyLog


class Email(MyLog, Confirmation):
    def __init__(self, email):
        super().__init__()
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, a):
        self._email = a

    def send(self, message):
        self.log.info(f"send email : {message} to {self.email} address")

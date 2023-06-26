from app.model.confirmation import Confirmation
from utils.my_log import MyLog


class Print(MyLog, Confirmation):
    def __init__(self):
        super().__init__()

    def send(self, message):
        self.log.info(f" print : {message}")

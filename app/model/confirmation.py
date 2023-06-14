from abc import ABC, abstractmethod


class Confirmation(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def send(self, message):
        raise NotImplementedError

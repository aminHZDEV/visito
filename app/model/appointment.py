from abc import ABC, abstractmethod
from app.db.base import Base


class Appointment(ABC, Base):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def appointment(self, payment: float = 0.0) -> bool:
        raise NotImplementedError

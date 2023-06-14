from app.db.base import Base


class Clinic(Base):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._clinic_id = 2

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def clinic_id(self):
        return self._clinic_id

    @clinic_id.setter
    def clinic_id(self, a):
        self._clinic_id = a

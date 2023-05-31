__author__ = "Fatemebagheri"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "fatemebagheri98@gmail.com"
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv
from app.db.base import Base

de = MyDotenv()


class Conditions(Base):
    def __init__(
        self,
        conditions_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        patient_name: str = "",
        condition: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._conditions_id = conditions_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._patient_name = patient_name
        self._condition = condition
        self._time = time

    @property
    def conditions_id(self):
        return self._conditions_id

    @conditions_id.setter
    def conditions_id(self, a):
        self._conditions_id = a

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, a):
        self._doctor_id = a

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, a):
        self._patient_id = a

    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, a):
        self._patient_name = a

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, a):
        self._condition = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add conditions model to database
        :return:
        """
        try:
            record = self.my_db[Conditions.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "patient_name": self.patient_name,
                    "condition": self.condition,
                }
            )
            self.conditions_id = record.inserted_id
            return self.conditions_id
        except Exception as e:
            self.log.error(e)
            return -1

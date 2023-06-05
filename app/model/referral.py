__author__ = "fatemebagheri"
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


class Referral(Base):
    def __init__(
        self,
        referral_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        patient_name: str = "",
        specialist_type: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._referral_id = referral_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._patient_name = patient_name
        self._specialist_type = specialist_type
        self._time = time

    @property
    def referral_id(self):
        return self._referral_id

    @referral_id.setter
    def referral_id(self, a):
        self._referral_id = a

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
    def specialist_type(self):
        return self._specialist_type

    @specialist_type.setter
    def specialist_type(self, a):
        self._specialist_type = a


    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add referral model to database
        :return:
        """
        try:
            record = self.my_db[Referral.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "patient_name": self.patient_name,
                    "specialist_type": self.specialist_type,

                }
            )
            self.referral_id = record.inserted_id
            return self.referral_id
        except Exception as e:
            self.log.error(e)
            return -1

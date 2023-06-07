__author__ = "Hatam"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "hatamabolghasemi@gmail.com"
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv
from app.db.base import Base

de = MyDotenv()


class Reference(Base):
    def __init__(
        self,
        reference_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        specialist: str = "",
        referral_request: str = "",
        specialist_office: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._reference_id = reference_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._specialist = specialist
        self._referral_request = referral_request
        self._specialist_office = specialist_office
        self._time = time

    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, a):
        self._reference_id = a

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
    def specialist(self):
        return self._specialist

    @specialist.setter
    def specialist(self, a):
        self._specialist = a

    @property
    def referral_request(self):
        return self._referral_request

    @referral_request.setter
    def referral_request(self, a):
        self._referral_request = a

    @property
    def specialist_office(self):
        return self._specialist_office

    @specialist_office.setter
    def specialist_office(self, a):
        self._specialist_office = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add reference model to database
        :return:
        """
        try:
            record = self.my_db[Reference.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "specialist": self.specialist,
                    "referral_request": self.referral_request,
                    "specialist_office": self.specialist_office,
                }
            )
            self.reference_id = record.inserted_id
            return self.reference_id
        except Exception as e:
            self.log.error(e)
            return -1

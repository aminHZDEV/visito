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


class InsuranceVerification(Base):
    def __init__(
        self,
        insurance_verification_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        insurance_information: str = "",
        receptionist: str = "",
        patient_copay_amount: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._insurance_verification_id = insurance_verification_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._insurance_information = insurance_information
        self._receptionist = receptionist
        self._patient_copay_amount = patient_copay_amount
        self._time = time

    @property
    def insurance_verification_id(self):
        return self._insurance_verification_id

    @insurance_verification_id.setter
    def insurance_verification_id(self, a):
        self._insurance_verification_id = a

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
    def insurance_information(self):
        return self._insurance_information

    @insurance_information.setter
    def insurance_information(self, a):
        self._insurance_information = a

    @property
    def receptionist(self):
        return self._receptionist

    @receptionist.setter
    def receptionist(self, a):
        self._receptionist = a

    @property
    def patient_copay_amount(self):
        return self._patient_copay_amount

    @patient_copay_amount.setter
    def patient_copay_amount(self, a):
        self._patient_copay_amount = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add insurance_verification model to database
        :return:
        """
        try:
            record = self.my_db[InsuranceVerification.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "insurance_information": self.insurance_information,
                    "receptionist": self.receptionist,
                    "patient_copay_amount": self.patient_copay_amount,
                }
            )
            self.insurance_verification_id = record.inserted_id
            return self.insurance_verification_id
        except Exception as e:
            self.log.error(e)
            return -1

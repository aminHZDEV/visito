__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv
from app.db.base import Base

de = MyDotenv()


class Visit(Base):
    def __init__(
        self,
        visit_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        symptom: str = "",
        diagnosis: str = "",
        medicine: str = "",
        time: str = datetime.now().strftime(de.mdotenv.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._visit_id = visit_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._symptom = symptom
        self._diagnosis = diagnosis
        self._medicine = medicine
        self._time = time

    @property
    def visit_id(self):
        return self._visit_id

    @visit_id.setter
    def visit_id(self, a):
        self._visit_id = a

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
    def symptom(self):
        return self._symptom

    @symptom.setter
    def symptom(self, a):
        self._symptom = a

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, a):
        self._diagnosis = a

    @property
    def medicine(self):
        return self._medicine

    @medicine.setter
    def medicine(self, a):
        self._medicine = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add visit model to database
        :return:
        """
        try:
            record = self.my_db[Visit.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "symptom": self.symptom,
                    "diagnosis": self.diagnosis,
                    "medicine": self.medicine,
                }
            )
            self.visit_id = record.inserted_id
            return self.visit_id
        except Exception as e:
            self.log.error(e)
            return -1

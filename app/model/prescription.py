__author__ = "narges-abbasii"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "nargesabbasi2976@gmail.com"
__status__ = "Production"

from datetime import datetime
from utils.my_dotenv import MyDotenv
from app.db.base import Base

de = MyDotenv()


class Prescription(Base):
    def __init__(
            self,
            prescription_id: int = -1,
            doctor_id: int = -1,
            patient_id: int = -1,
            dosage: str = "",
            diagnosis: str = "",
            drug: str = "",
            time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._prescription_id = prescription_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._dosage = dosage
        self._diagnosis = diagnosis
        self._drug = drug
        self._time = time

    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def visit_id(self, a):
        self._prescription_id = a

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
    def dosage(self):
        return self._dosage

    @dosage.setter
    def dosage(self, a):
        self._dosage = a

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, a):
        self._diagnosis = a

    @property
    def drug(self):
        return self._drug

    @drug.setter
    def drug(self, a):
        self._drug = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add prescription model to database
        :return:
        """
        try:
            record = self.my_db[Prescription.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "diagnosis": self.diagnosis,
                    "dosage": self.dosage,
                    "drug": self.drug,

                }
            )
            self._prescription_id = record.inserted_id
            return self.prescription_id
        except Exception as e:
            self.log.error(e)
            return -1

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


class TestResults(Base):
    def __init__(
        self,
        test_result_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        medical_test: str = "",
        results: str = "",
        medicine: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._test_result_id = test_result_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._medical_test = medical_test
        self._results = results
        self._medicine = medicine
        self._time = time

    @property
    def test_result_id(self):
        return self._test_result_id

    @test_result_id.setter
    def test_result_id(self, a):
        self._test_result_id = a

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
    def medical_test(self):
        return self._medical_test

    @medical_test.setter
    def medical_test(self, a):
        self._medical_test = a

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, a):
        self._results = a

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
        this method add test_result model to database
        :return:
        """
        try:
            record = self.my_db[TestResults.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "medical_test": self.medical_test,
                    "results": self.results,
                    "medicine": self.medicine,
                }
            )
            self.test_result_id = record.inserted_id
            return self.test_result_id
        except Exception as e:
            self.log.error(e)
            return -1

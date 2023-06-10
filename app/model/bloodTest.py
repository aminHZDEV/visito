__author__ = "isaac1998sm"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "isaacsalmanpour@gmail.com"
__status__ = "Production"

from app.db.base import Base


class BloodTest(Base):
    def __init__(
        self,
        blood_test_id: int = -1,
        result: str = "",
        purpose: str = "",
        location: str = "",
        date: str = "",
        time: str = "",
        doctor_id: int = -1,
        patient_id: int = -1,
        medicine: str = "",
    ):
        super().__init__()
        self._blood_test_id = blood_test_id
        self._result = result
        self._purpose = purpose
        self._location = location
        self._date = date
        self._time = time
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._medicine = medicine

    @property
    def blood_test_id(self):
        return self._blood_test_id

    @blood_test_id.setter
    def blood_test_id(self, blood_test_id):
        self._blood_test_id = blood_test_id

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        self._purpose = purpose

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, doctor_id):
        self._doctor_id = doctor_id

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id

    @property
    def medicine(self):
        return self._medicine

    @medicine.setter
    def medicine(self, medicine):
        self._medicine = medicine

    def add(self) -> int:
        """
        this method add blood test model to database
        :return:
        """
        try:
            record = self.my_db[BloodTest.__name__].insert_one(
                {
                    "time": self.time,
                    "result": self.result,
                    "purpose": self.purpose,
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "date": self.date,
                    "medicine": self.medicine,
                    "location": self.location
                }
            )
            self.blood_test_id = record.inserted_id
            return self.blood_test_id
        except Exception as e:
            self.log.error(e)
            return -1

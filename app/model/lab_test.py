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


class Lab_test(Base):
    def __init__(
            self,
            lab_test_id: int = -1,
            doctor_id: int = -1,
            patient_id: int = -1,
            patient_name: str = "",
            test_type: str = "",
            time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._lab_test_id = lab_test_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._patient_name = patient_name
        self._test_type = test_type
        self._time = time

    @property
    def lab_test_id(self):
        return self._lab_test_id

    @lab_test_id.setter
    def lab_test_id(self, a):
        self._lab_test_id = a

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
    def test_type(self):
        return self._test_type

    @test_type.setter
    def test_type(self, a):
        self._test_type = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add lab_test model to database
        :return:
        """
        try:
            record = self.my_db[Lab_test.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "patient_name": self.patient_name,
                    "test_type": self.test_type,

                }
            )
            self._lab_test_id = record.inserted_id
            return self.lab_test_id
        except Exception as e:
            self.log.error(e)
            return -1

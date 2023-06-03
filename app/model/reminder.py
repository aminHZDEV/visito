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


class Reminder(Base):
    def __init__(
        self,
        reminder_id: int = -1,
        doctor_id: int = -1,
        patient_id: int = -1,
        appointment_details: str = "",
        contact_details: str = "",
        time: str = datetime.now().strftime(de.dotenv_values.get("TIME_FORMAT")),
    ):
        super().__init__()
        self._reminder_id = reminder_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._appointment_details = appointment_details
        self._contact_details = contact_details
        self._time = time

    @property
    def reminder_id(self):
        return self._reminder_id

    @reminder_id.setter
    def reminder_id(self, a):
        self._reminder_id = a

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
    def appointment_details(self):
        return self._appointment_details

    @appointment_details.setter
    def appointment_details(self, a):
        self._appointment_details = a

    @property
    def contact_details(self):
        return self._contact_details

    @contact_details.setter
    def contact_details(self, a):
        self._contact_details = a

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, a):
        self._time = a

    def add(self) -> int:
        """
        this method add reminder model to database
        :return:
        """
        try:
            record = self.my_db[Reminder.__name__].insert_one(
                {
                    "doctor_id": self.doctor_id,
                    "patient_id": self.patient_id,
                    "appointment_details": self.appointment_details,
                    "contact_details": self.contact_details,
                }
            )
            self.reminder_id = record.inserted_id
            return self.reminder_id
        except Exception as e:
            self.log.error(e)
            return -1

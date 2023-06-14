from app.model.appointment import Appointment


class Offer(Appointment):
    def __init__(
        self,
        clinic: object = None,
        patient: object = None,
        time_slot: str = "",
        date: str = "",
    ):
        super().__init__()
        self._clinic = clinic
        self._patient = patient
        self._time_slot = time_slot
        self._date = date
        self._payment = 0.0

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, a):
        self._payment = a

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, a):
        self._patient = a

    @property
    def time_slot(self):
        return self._time_slot

    @time_slot.setter
    def time_slot(self, a):
        self._time_slot = a

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, a):
        self._date = a

    @property
    def clinic(self):
        return self._clinic

    @clinic.setter
    def clinic(self, a):
        self._clinic = a

    # def confirm(self, choose: bool = True) -> bool:
    #     return choose

    def appointment(self, payment: float = 0.0) -> int:
        self.payment = payment
        try:
            record = self.my_db["appointment"].insert_one(
                {
                    "patient_id": self.patient.id_cart,
                    "clinic_id": self.clinic.clinic_id,
                    "time_slot": self.time_slot,
                    "date": self.date,
                    "payment": self.payment,
                }
            )
            self.appointment_id = record.inserted_id
            return self.appointment_id
        except Exception as e:
            self.log.error(e)
            return -1

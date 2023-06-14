import pytest
from utils.fakes import FAKE_DB

from app.model.appointment import Appointment
from app.model.patient import Patient
from app.model.doctor import Doctor
from utils.status import InsertStatus, FindStatus

_valid_patient = Patient(name='valid_1', ssid='valid_1')
_valid_patient.add(update=False)
_valid_doctor = Doctor(name='dr. valid_1', gmc_number='valid_1', field='valid field')
_valid_doctor.add(update=False)

params_add = [(Appointment(patient=_valid_patient, doctor=_valid_doctor, date='2023-09-09 01:00 AM'), InsertStatus.INSERTED_SUCCESSFULLY),
              (Appointment(patient=_valid_patient, doctor=_valid_doctor, date='2023-09-09 01:00 AM'), InsertStatus.DUPLICATE_ENTRY),
              (Appointment(), InsertStatus.INCOMPLETE_INFO),
              (Appointment(patient=_valid_patient, doctor=_valid_doctor, id_cart=FAKE_DB['Appointment'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Appointment(patient=_valid_patient, doctor=_valid_doctor, date='2023-09-09 01:00 AM'), FindStatus.RECORD_FOUND),
               (Appointment(patient=Patient(id_cart=25), doctor=Doctor(id_cart='InvalidID')), FindStatus.NO_RECORDS),
               (Appointment(id_cart=FAKE_DB['Appointment'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Appointment(id_cart='InvalidID'), FindStatus.NO_RECORDS),
               (Appointment(), FindStatus.INSUFFICIENT_INFO)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

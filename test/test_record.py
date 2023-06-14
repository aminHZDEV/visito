import pytest
from utils.fakes import FAKE_DB

from app.model.record import Record
from app.model.patient import Patient
from utils.status import InsertStatus, FindStatus

_valid_patient = Patient(name='Patient_1', ssid='SSID_1')
_valid_patient.find_and_update()

params_add = [(Record(patient=_valid_patient, token='123456789', info='Some info', date='2023-06-14 10:00 AM'), InsertStatus.INSERTED_SUCCESSFULLY),
              (Record(patient=_valid_patient, token='123456789', info='Some info', date='2023-06-14 10:00 AM'), InsertStatus.DUPLICATE_ENTRY),
              (Record(), InsertStatus.INCOMPLETE_INFO),
              (Record(patient=_valid_patient, token='123456789', info='Some info', date='2023-06-14 10:00 AM', id_cart=FAKE_DB['Invoice'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Record(token='123456789'), FindStatus.RECORD_FOUND),
               (Record(token='NonExistent'), FindStatus.NO_RECORDS),
               (Record(id_cart=FAKE_DB['Record'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Record(id_cart='InvalidID'), FindStatus.NO_RECORDS),
               (Record(), FindStatus.INSUFFICIENT_INFO)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

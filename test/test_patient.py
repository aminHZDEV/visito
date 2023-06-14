import pytest
from utils.fakes import FAKE_DB

from app.model.patient import Patient
from utils.status import InsertStatus, FindStatus

params_add = \
    [(Patient(name='Patient_3', ssid='SSID_3'), InsertStatus.INSERTED_SUCCESSFULLY),
     (Patient(name='Patient_4', ssid='SSID_1'), InsertStatus.DUPLICATE_ENTRY),
     (Patient(), InsertStatus.INCOMPLETE_INFO),
     (Patient(name='Patient_5', ssid='SSID_5', id_cart=FAKE_DB['Patient'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Patient(name='Patient_1', ssid='SSID_1'), FindStatus.RECORD_FOUND),
               (Patient(ssid='SSID_10'), FindStatus.NO_RECORDS),
               (Patient(id_cart=FAKE_DB['Patient'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Patient(id_cart=125), FindStatus.NO_RECORDS)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

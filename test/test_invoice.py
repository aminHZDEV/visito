import pytest
from utils.fakes import FAKE_DB

from app.model.invoice import Invoice
from app.model.patient import Patient
from utils.status import InsertStatus, FindStatus

_valid_patient = Patient(name='Patient_1', ssid='SSID_1')
_valid_patient.find_and_update()

params_add = [(Invoice(patient=_valid_patient, service='Service_4', amount=80, invoice_number='INV-0003'), InsertStatus.INSERTED_SUCCESSFULLY),
              (Invoice(patient=_valid_patient, service='Service_4', amount=80, invoice_number='INV-0001'), InsertStatus.DUPLICATE_ENTRY),
              (Invoice(), InsertStatus.INCOMPLETE_INFO),
              (Invoice(patient=_valid_patient, service='Service_4', amount=80, invoice_number='INV-0005', id_cart=FAKE_DB['Invoice'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Invoice(invoice_number='INV-0001'), FindStatus.RECORD_FOUND),
               (Invoice(invoice_number='NonExistent'), FindStatus.NO_RECORDS),
               (Invoice(id_cart=FAKE_DB['Invoice'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Invoice(id_cart='InvalidID'), FindStatus.NO_RECORDS),
               (Invoice(), FindStatus.INSUFFICIENT_INFO)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

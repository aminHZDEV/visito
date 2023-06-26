import pytest

from app.model.payment import Payment
from utils.fakes import FAKE_DB
from utils.status import InsertStatus, FindStatus

params_add = [
    (Payment(invoice_number='INV-0001', amount=100, date='2023-09-09 11:00 PM'), InsertStatus.INSERTED_SUCCESSFULLY),
    (Payment(invoice_number='INV-0001', amount=100, date='2023-09-09 11:00 PM'), InsertStatus.DUPLICATE_ENTRY),
    (Payment(), InsertStatus.INCOMPLETE_INFO),
    (Payment(invoice_number='INV-0005', amount=100, date='2023-09-09 11:00 PM',
             id_cart=FAKE_DB['Payment'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Payment(invoice_number='INV-0001', amount=50, date='2023-01-01 12:00 AM'), FindStatus.RECORD_FOUND),
               (Payment(invoice_number='NonExistent', amount=50, date='2023-09-09 12:00 PM'), FindStatus.NO_RECORDS),
               (Payment(id_cart=FAKE_DB['Payment'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Payment(id_cart='InvalidID'), FindStatus.NO_RECORDS),
               (Payment(), FindStatus.INSUFFICIENT_INFO)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

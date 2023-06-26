import pytest

from app.model.medicine import Medicine
from utils.fakes import FAKE_DB
from utils.status import InsertStatus, FindStatus

params_add = [(Medicine(name='Item_3', quantity=10), InsertStatus.INSERTED_SUCCESSFULLY),
              (Medicine(name='Item_1', quantity=20), InsertStatus.DUPLICATE_ENTRY),
              (Medicine(), InsertStatus.INCOMPLETE_INFO),
              (Medicine(name='Item_20', quantity=60, id_cart=FAKE_DB['Medicine'].find_one({})['_id']),
               InsertStatus.DUPLICATE_ID)]

params_find = [(Medicine(name='Item_1'), FindStatus.RECORD_FOUND),
               (Medicine(name='Item_10'), FindStatus.NO_RECORDS),
               (Medicine(id_cart=FAKE_DB['Medicine'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Medicine(id_cart='InvalidID'), FindStatus.NO_RECORDS)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

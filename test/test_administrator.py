import pytest
from utils.fakes import FAKE_DB

from app.model.administrator import Administrator
from utils.status import InsertStatus, FindStatus

params_add = \
    [(Administrator(name='Admin_3', username='Username_3', password='Password_3'), InsertStatus.INSERTED_SUCCESSFULLY),
     (Administrator(name='Admin_1', username='Username_4', password='Password_4'), InsertStatus.INSERTED_SUCCESSFULLY),
     (Administrator(name='Admin_4', username='Username_1', password='Password_4'), InsertStatus.DUPLICATE_ENTRY),
     (Administrator(), InsertStatus.INCOMPLETE_INFO),
     (Administrator(name='Admin_5', username='Username_5', password='Password_5', id_cart=FAKE_DB['Administrator'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Administrator(username='Username_1'), FindStatus.RECORD_FOUND),
               (Administrator(username='Username_10'), FindStatus.NO_RECORDS),
               (Administrator(id_cart=FAKE_DB['Administrator'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Administrator(id_cart='InvalidID'), FindStatus.NO_RECORDS)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

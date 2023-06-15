import pytest
from utils.fakes import FAKE_DB

from app.model.doctor import Doctor
from utils.status import InsertStatus, FindStatus

params_add = \
    [(Doctor(name='Doctor_1', gmc_number='7777777', field='Orthopedist'), InsertStatus.INSERTED_SUCCESSFULLY),
     (Doctor(name='Doctor_2', gmc_number='8888888', field='Neurologist'), InsertStatus.INSERTED_SUCCESSFULLY),
     (Doctor(name='Doctor_1', gmc_number='7777777', field='Orthopedist'), InsertStatus.DUPLICATE_ENTRY),
     (Doctor(), InsertStatus.INCOMPLETE_INFO),
     (Doctor(name='Doctor_1', gmc_number='7777777', field='Orthopedist', id_cart=FAKE_DB['Doctor'].find_one({})['_id']), InsertStatus.DUPLICATE_ID)]

params_find = [(Doctor(gmc_number='GMC_1'), FindStatus.RECORD_FOUND),
               (Doctor(gmc_number='NonExistentGMC'), FindStatus.NO_RECORDS),
               (Doctor(id_cart=FAKE_DB['Doctor'].find_one({})['_id']), FindStatus.RECORD_FOUND),
               (Doctor(id_cart='InvalidID'), FindStatus.NO_RECORDS)]


@pytest.mark.parametrize("test_input, expected", params_add)
def test_insertion(test_input, expected):
    assert test_input.add(update=False) is expected


@pytest.mark.parametrize("test_input, expected", params_find)
def test_lookup(test_input, expected):
    assert test_input.find_and_update() is expected

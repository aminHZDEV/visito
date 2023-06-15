import pytest
from app.model.bill import Bill
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("doctor_test_case.csv")


@pytest.mark.parametrize(titles, testcases)
def test_bill_generation(name, expected):
    bill = Bill(name=name)
    assert bill.add() != expected
    log.log.info(
        f"pytest doctor add function pass name :  {name} != expected {expected} \n"
    )
import pytest
from app.model.bill import Bill
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("bill_test_case.csv")


@pytest.mark.parametrize(titles, testcases)
def test_bill_generation(duration ,amount , expected):
    bill = Bill(
           duration=duration,
           amount=amount,
        )
    assert bill.add() != expected
    log.log.info(
        f"pytest generate bill  pass != expected {expected} \n"
    )
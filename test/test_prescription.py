import pytest
from app.model.refill import Refill
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("prescription_refill_request.csv")


@pytest.mark.parametrize(titles, testcases)
def test_reminder_add(prescription_details, expected):
    refill = Refill(prescription_details=prescription_details)
    assert refill.add() != expected
    log.log.info(
        f"pytest prescription details add function pass name :  {prescription_details} != expected {expected} \n"
    )

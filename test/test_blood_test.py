import pytest
from app.model.bloodTest import BloodTest
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("appointment.csv")


@pytest.mark.parametrize(titles, testcases)
def test_appointment_add(result, expected):
    test = BloodTest(medicine="asprine")
    assert test.add() != expected
    log.log.info(f"test blood test passed. {result} != {expected} as expected\n")
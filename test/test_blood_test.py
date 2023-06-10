import pytest
from app.model.bloodTest import BloodTest
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("blood_test_test_case.csv")


@pytest.mark.parametrize(titles, testcases)
def test_appointment_add(medicine, expected):
    test = BloodTest(medicine=medicine)
    assert test.add() != expected
    log.log.info(f"test blood test passed. {medicine} != {expected} as expected\n")

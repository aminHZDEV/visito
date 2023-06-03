import pytest
from app.model.result_of_tests import TestResults
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("results_of_test.csv")


@pytest.mark.parametrize(titles, testcases)
def test_reminder_add(medical_test, expected):
    medical_test_result = TestResults(medical_test=medical_test)
    assert medical_test_result.add() != expected
    log.log.info(
        f"pytest medical test add function pass name :  {medical_test} != expected {expected} \n"
    )

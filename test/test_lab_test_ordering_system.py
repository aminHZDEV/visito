import pytest
from app.model.lab_test import Lab_test
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("lab_test_test_case.csv")

@pytest.mark.parametrize(titles, testcases)
def test_order_lab_test(test_type, expected):
    lab_test = Lab_test(test_type=test_type)
    assert lab_test.add() != expected
    log.log.info(f"pytest lab_test add function pass test_type :  {test_type} != expected {expected} \n")

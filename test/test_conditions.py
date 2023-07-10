import pytest
from app.model.conditions import Conditions
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("medical_history_management_with_conditions.csv")


@pytest.mark.parametrize(titles, testcases)
def test_conditions_add(condition, expected):
    conditions = Conditions(condition=condition)
    assert conditions.add() != expected
    log.log.info(
        f"pytest prescription details add function pass condition :  {condition} != expected {expected} \n"
    )

import pytest
from app.model.referral import Referral
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("patient_referral_test_case.csv")


@pytest.mark.parametrize(titles, testcases)
def test_referral_add(specialist_type,expected):
    referral = Referral(specialist_type=specialist_type)
    assert referral.add() != expected
    log.log.info(
        f"pytest Referral details add function pass specialist_type :  {specialist_type} != expected {expected} \n"
    )
import pytest
from app.model.reference import Reference
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("medical_referral.csv")


@pytest.mark.parametrize(titles, testcases)
def test_reminder_add(referral_request, expected):
    medical_referral = Reference(referral_request=referral_request)
    assert medical_referral.add() != expected
    log.log.info(
        f"pytest medical referral add function pass name :  {referral_request} != expected {expected} \n"
    )

import pytest
from app.model.insurance_verification import InsuranceVerification
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("insurance_verification.csv")


@pytest.mark.parametrize(titles, testcases)
def test_reminder_add(insurance_information, expected):
    insurance_verification = InsuranceVerification(insurance_information=insurance_information)
    assert insurance_verification.add() != expected
    log.log.info(
        f"pytest insruance verification add function pass name :  {insurance_information} != expected {expected} \n"
    )

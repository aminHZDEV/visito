import pytest
from app.model.patient import Patient
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("height_wieght_test_case.csv")


@pytest.mark.parametrize(titles, testcases)
def test_height_weight(patient_id ,height, weight, expected):

    #update = Patient.update_height_weight(patient_id, height, weight)

    assert Patient.update_height_weight(patient_id, height, weight) != expected
    log.log.info(
        f"pytest updated patient with id {patient_id}  != expected {expected} \n"
    )
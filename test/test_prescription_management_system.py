import pytest
from app.model.prescription import Prescription
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("drug_and_dosage_information_test_case.csv")

@pytest.mark.parametrize(titles, testcases)
def test_prescribe_medication(drug, dosage, expected):
    prescription = Prescription(drug=drug, dosage=dosage)
    assert prescription.add() != expected
    log.log.info(f"pytest prescription add function pass drug dosage information :  {drug, dosage} != expected {expected} \n")

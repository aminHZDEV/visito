__author__ = "isaac1998sm"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "isaacsalmanpour@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher

from app.model.bloodTest import BloodTest
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.visit import Visit
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("a patient named (?P<name>.+) who has done a blood test")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    record = base.my_db[Patient.__name__].insert_one({"name": name})
    context.patient = Patient(name=name, id_cart=record.inserted_id)
    log.log.info(f"{name} has done a blood test")


@when("the doctor receives the blood test results from the laboratory as (?P<blood_test_result>.+)")
def step_impl(context, blood_test_result):
    """
    :type context: behave.runner.Context
    :type blood_test_result: str
    """
    name = names.get_full_name()
    record = base.my_db[Doctor.__name__].insert_one({"name": name})
    context.doctor = Doctor(name=name, id_cart=record.inserted_id)
    context.blood_test_result = blood_test_result
    log.log.info(f"the doctor {context.doctor.name} receives the blood test results from the laboratory as {blood_test_result}")


@then("if necessary, prescribe (?P<medication>.+) or further tests for them\.")
def step_impl(context, medication):
    """
    :type context: behave.runner.Context
    :type medication: str
    """
    record = base.my_db[BloodTest.__name__].insert_one(
        {
            "result": context.blood_test_result,
            "doctor_id": context.doctor.id_cart,
            "patient_id": context.patient.id_cart,
            "medicine": medication,
        }
    )
    context.blood_test = BloodTest(
        blood_test_id=record.inserted_id,
        result=context.blood_test_result,
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        medicine=medication,
    )
    record = base.my_db[BloodTest.__name__].find_one({"_id": context.blood_test.blood_test_id})
    assert context.blood_test.blood_test_id == record["_id"]
    assert context.blood_test.doctor_id == record["doctor_id"]
    assert context.blood_test.patient_id == record["patient_id"]
    assert context.blood_test.medicine == record["medicine"]
    log.log.info(f"the doctor {context.doctor.name} prescribes {medication} for {context.patient.name} with blood test result {context.blood_test.result}")
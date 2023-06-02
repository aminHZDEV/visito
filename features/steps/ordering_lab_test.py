__author__ = "narges-abbasii"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "nargesabbasi2976@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.lab_test import Lab_test
import names

use_step_matcher("re")

base = Base()
log = MyLog()



@given('I am a doctor and i want to order a lab test for a patient.')
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    log.log.info(f"I am a doctor {context.doctor.name} and i want to order a lab test for a {context.patient.name} ")


@when('I enter the patient\'s information (?P<patient_name>.+) and the (?P<test_type>.+)')
def step_impl(context, patient_name, test_type):
    context.patient_name = patient_name
    context.test_type = test_type
    log.log.info(f'Create a new lab test order for the {patient_name} and {test_type}')


@then('the test should be ordered successfully')
# Check that the lab test order was created successfully
def step_impl(context):
    lab_test = Lab_test(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        patient_name=context.patient_name,
        test_type=context.test_type,
    )
    lab_test_id = lab_test.add()
    context.lab_test = lab_test
    search_lab_test = base.my_db[Lab_test.__name__].find_one({"_id": lab_test_id})
    assert lab_test.lab_test_id == search_lab_test["_id"]
    assert context.lab_test.doctor_id == search_lab_test["doctor_id"]
    assert context.lab_test.patient_id == search_lab_test["patient_id"]
    assert context.lab_test.patient_name == search_lab_test["patient_name"]
    assert context.lab_test.test_type == search_lab_test["test_type"]
    log.log.info(f"the test should be ordered successfully")

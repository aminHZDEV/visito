__author__ = "Fatemebagheri"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "fatemebagheri98@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.conditions import Conditions
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("I am a doctor")
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"I am a doctor")

@given("I want to add a medical condition to a patient's record")
def step_impl(context):
    log.log.info(f"I want to add a medical condition to a patient's record")


@when("I enter the patient's information (?P<patient_name>.+) and medical condition (?P<condition>.+)")
def step_impl(context, patient_name, condition):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.patient_name = patient_name
    context.condition = condition
    log.log.info(f"I enter the patient's information {patient_name} and medical condition{condition}")


@then("the condition added successfully")
def step_impl(context):
    conditions = Conditions(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        patient_name=context.patient_name,
        condition=context.condition,
    )
    conditions_id = conditions.add()
    context.conditions = conditions
    search_conditions = base.my_db[Conditions.__name__].find_one({"_id": conditions_id})
    assert context.conditions.conditions_id == search_conditions["_id"]
    assert context.conditions.doctor_id == search_conditions["doctor_id"]
    assert context.conditions.patient_id == search_conditions["patient_id"]
    assert context.conditions.patient_name == search_conditions["patient_name"]
    assert context.conditions.condition == search_conditions["condition"]
    log.log.info(f"the condition added successfully at {context.conditions.time}")



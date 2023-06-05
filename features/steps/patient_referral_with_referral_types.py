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
from app.model.referral import Referral
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("Im a doctor")
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"Im a doctor")
@given("I want to refer a patient to a specialist")
def step_impl(context):
    log.log.info(f"I want to refer a patient to a specialist")

@when("I enter the patient's information(?P<patient_name>.+) and the specialist type(?P<specialist_type>.+)")
def step_impl(context, patient_name, specialist_type):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.patient_name = patient_name
    context.specialist_type = specialist_type
    log.log.info(f"I enter the patient's information {patient_name} and the specialist type {specialist_type}")


@then("the referral made successfully")
def step_impl(context):
    referral = Referral(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        patient_name=context.patient_name,
        specialist_type=context.specialist_type,
    )
    referral_id = referral.add()
    context.referral = referral
    search_referral = base.my_db[Referral.__name__].find_one({"_id": referral_id})
    assert context.referral.referral_id == search_referral["_id"]
    assert context.referral.doctor_id == search_referral["doctor_id"]
    assert context.referral.patient_id == search_referral["patient_id"]
    assert context.referral.patient_name == search_referral["patient_name"]
    assert context.referral.specialist_type == search_referral["specialist_type"]
    log.log.info(f"the referral made successfully at {context.referral.time}")


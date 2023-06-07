__author__ = "Hatam"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "hatamabolghasemi@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.reference import Reference
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given('the doctor recommends a referral to (?P<specialist>.+)')
def step_impl(context, specialist):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.specialist = specialist
    log.log.info(f"the doctor recommends a referral to {specialist}")


@when('the system generates a (?P<referral_request>.+)')
def step_impl(context, referral_request):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    context.referral_request = referral_request
    log.log.info(f"the system generates a {referral_request}")

@then('the system should send the referral request to the (?P<specialist_office>.+)')
def step_impl(context, specialist_office):
    context.specialist_office = specialist_office
    reference = Reference(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        specialist_office=context.specialist_office,
        referral_request=context.referral_request,
        specialist=context.specialist,
    )
    reference_id = reference.add()
    context.reference = reference
    search_reference = base.my_db[Reference.__name__].find_one({"_id": reference_id})
    assert context.reference.reference_id == search_reference["_id"]
    assert context.reference.doctor_id == search_reference["doctor_id"]
    assert context.reference.patient_id == search_reference["patient_id"]
    assert context.reference.referral_request == search_reference["referral_request"]
    assert context.reference.specialist_office == search_reference["specialist_office"]
    assert context.reference.specialist == search_reference["specialist"]
    log.log.info(f"the system should send the referral request to the {specialist_office}")

@then('the system should notify the patient of the referral request')
def step_impl(context):
    log.log.info(f"the system should notify the patient of the referral request")

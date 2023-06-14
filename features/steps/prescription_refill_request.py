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
from app.model.refill import Refill
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("the patient wants to request a prescription refill")
def step_patient_wants_to_request_prescription_refill(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"the patient wants to request a prescription refill")


@when("the patient requests a refill for (?P<medication_name>.+)")
def step_patient_requests_refill_for_medication(context, medication_name):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.medication_name = medication_name
    log.log.info(f"the patient requests a refill for {medication_name}")


@then("the system should confirm the (?P<prescription_details>.+)")
def step_system_confirms_prescription_details(context, prescription_details):
    context.prescription_details = prescription_details
    log.log.info(f"the system should confirm the {prescription_details}")


@then("the system should send a prescription refill request to the doctor for approval")
def step_system_sends_request_to_doctor_for_approval(context):
    refill = Refill(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        medication_name=context.medication_name,
        prescription_details=context.prescription_details,
    )
    refill_id = refill.add()
    context.refill = refill
    search_refill = base.my_db[Refill.__name__].find_one({"_id": refill_id})
    assert context.refill.refill_id == search_refill["_id"]
    assert context.refill.doctor_id == search_refill["doctor_id"]
    assert context.refill.patient_id == search_refill["patient_id"]
    assert context.refill.prescription_details == search_refill["prescription_details"]
    assert context.refill.medication_name == search_refill["medication_name"]
    log.log.info(
        f"the system should send a prescription refill request to the doctor for approval"
    )

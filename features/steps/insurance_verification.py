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
from app.model.insurance_verification import InsuranceVerification
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given('the patient wants to verify their (?P<insurance_information>.+)')
def step_patient_wants_to_verify_insurance_information(context, insurance_information):
    # Perform necessary actions here
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.insurance_information = insurance_information
    log.log.info(f"the patient wants to verify their {insurance_information}")

@when("the (?P<receptionist>.+) enters the patient's insurance information")
def step_receptionist_enters_patient_insurance_information(context, receptionist):
    # Retrieve the entered insurance information and perform necessary actions here
    context.receptionist = receptionist
    log.log.info(f"the {receptionist} enters the patient's insurance information")

@then('the system should confirm the insurance details and display the (?P<patient_copay_amount>.+)')
def step_system_confirms_insurance_details(context, patient_copay_amount):
    # Verify the insurance details and perform necessary actions here
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    context.patient_copay_amount = patient_copay_amount
    insurance_verification = InsuranceVerification(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        insurance_information=context.insurance_information,
        receptionist=context.receptionist,
        patient_copay_amount=context.patient_copay_amount,
    )
    insurance_verification_id = insurance_verification.add()
    context.insurance_verification = insurance_verification
    search_insurance_verification = base.my_db[InsuranceVerification.__name__].find_one({"_id": insurance_verification_id})
    assert context.insurance_verification.insurance_verification_id == search_insurance_verification["_id"]
    assert context.insurance_verification.doctor_id == search_insurance_verification["doctor_id"]
    assert context.insurance_verification.patient_id == search_insurance_verification["patient_id"]
    assert context.insurance_verification.receptionist == search_insurance_verification["receptionist"]
    assert context.insurance_verification.insurance_information == search_insurance_verification["insurance_information"]
    assert context.insurance_verification.patient_copay_amount == search_insurance_verification["patient_copay_amount"]
    log.log.info(f"the system should confirm the insurance details and display the {patient_copay_amount}")

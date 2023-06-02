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
from app.model.prescription import Prescription
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given('I\'m doctor')
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"I am a doctor {context.doctor.name}.")

@given('I want to write a prescription for a patient')
def step_impl(context):
    log.log.info('I want to write a prescription for a patient')


@when('I enter the patients information')
def step_impl(context):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    log.log.info(f"I enter the patient's information {context.patient.name}.")


@when('I prescribe (?P<drug>.+) with (?P<dosage>.+)')
def step_impl(context, drug, dosage):
    context.drug = drug
    context.dosage = dosage
    log.log.info(f"the doctor should prescribe drug{drug} and dosage {dosage} ")

@then('the prescription should be written successfully')
def step_impl(context):
    prescription = Prescription(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        drug=context.drug,
        dosage=context.dosage,

    )
    prescription_id = prescription.add()
    context.prescription = prescription
    search_prescription = base.my_db[Prescription.__name__].find_one({"_id": prescription_id})
    assert prescription.prescription_id == search_prescription["_id"]
    assert context.prescription.doctor_id == search_prescription["doctor_id"]
    assert context.prescription.patient_id == search_prescription["patient_id"]
    assert context.prescription.drug == search_prescription["drug"]
    log.log.info(f"the prescription should be written successfully")

__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.visit import Visit
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("the patient has (?P<symptom>.+)")
def step_impl(context, symptom):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.symptom = symptom
    log.log.info(f"the patient has {symptom}")


@when("the doctor examines the patient")
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"the doctor examines the patient")


@then("the doctor should be able to diagnose (?P<diagnosis>.+)")
def step_impl(context, diagnosis):
    context.diagnosis = diagnosis
    log.log.info(f"the doctor should be able to diagnose {diagnosis}")


@then("the doctor should prescribe (?P<medicine>.+)")
def step_impl(context, medicine):
    visit = Visit(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        symptom=context.symptom,
        medicine=medicine,
        diagnosis=context.diagnosis,
    )
    visit_id = visit.add()
    context.visit = visit
    search_visit = base.my_db[Visit.__name__].find_one({"_id": visit_id})
    assert context.visit.visit_id == search_visit["_id"]
    assert context.visit.doctor_id == search_visit["doctor_id"]
    assert context.visit.patient_id == search_visit["patient_id"]
    assert context.visit.medicine == search_visit["medicine"]
    assert context.visit.symptom == search_visit["symptom"]
    assert context.visit.diagnosis == search_visit["diagnosis"]
    log.log.info(f"the doctor should prescribe {medicine} ")
    log.log.info(
        f"the patient {context.patient.name} examine successfully by doctor {context.doctor.name} at {context.visit.time}"
    )

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
    record = base.my_db[Patient.__name__].insert_one({"name": name})
    context.patient = Patient(name=name, id_cart=record.inserted_id)
    context.symptom = symptom
    log.log.info(f"the patient has {symptom}")


@when("the doctor examines the patient")
def step_impl(context):
    name = names.get_full_name()
    record = base.my_db[Doctor.__name__].insert_one({"name": name})
    context.doctor = Doctor(name=name, id_cart=record.inserted_id)
    log.log.info(f"the doctor examines the patient")


@then("the doctor should be able to diagnose (?P<diagnosis>.+)")
def step_impl(context, diagnosis):
    context.diagnosis = diagnosis
    log.log.info(f"the doctor should be able to diagnose {diagnosis}")


@then("the doctor should prescribe (?P<medicine>.+)")
def step_impl(context, medicine):
    record = base.my_db[Visit.__name__].insert_one(
        {
            "doctor_id": context.doctor.id_cart,
            "patient_id": context.patient.id_cart,
            "symptom": context.symptom,
            "diagnosis": context.diagnosis,
            "medicine": medicine,
        }
    )

    context.visit = Visit(
        visit_id=record.inserted_id,
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        symptom=context.symptom,
        medicine=medicine,
        diagnosis=context.diagnosis,
    )
    record = base.my_db[Visit.__name__].find_one({"_id": context.visit.visit_id})
    assert context.visit.visit_id == record["_id"]
    assert context.visit.doctor_id == record["doctor_id"]
    assert context.visit.patient_id == record["patient_id"]
    assert context.visit.medicine == record["medicine"]
    assert context.visit.symptom == record["symptom"]
    assert context.visit.diagnosis == record["diagnosis"]
    log.log.info(f"the doctor should prescribe {medicine} ")
    log.log.info(
        f"the patient {context.patient.name} examine successfully by doctor {context.doctor.name} at {context.visit.time}"
    )

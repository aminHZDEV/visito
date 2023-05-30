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
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("a patient named (?P<name>.+) who needs a blood test")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    record = base.my_db[Patient.__name__].insert_one({"name": name})
    context.patient = Patient(name=name, id_cart=record.inserted_id)
    log.log.info(f"patient {name} needs a blood test")


@when("the doctor orders a blood test for the patient")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    name = names.get_full_name()
    record = base.my_db[Doctor.__name__].insert_one({"name": name})
    context.doctor = Doctor(name=name, id_cart=record.inserted_id)
    log.log.info(f"the doctor {context.doctor.name} orders a blood test for the patient {context.patient.name}")


@then(
    "the doctor should inform the patient about the blood test procedure and purpose as checking their (?P<blood_test_purpose>.+)")
def step_impl(context, blood_test_purpose):
    """
    :type context: behave.runner.Context
    :type blood_test_purpose: str
    """
    context.blood_test_purpose = blood_test_purpose
    log.log.info(f"doctor {context.doctor.name} tells to patient {context.patient.name} that blood test procedure and purpose is {blood_test_purpose}")


@then(
    "the doctor should tell the patient to go to (?P<blood_test_location>.+) on (?P<date>.+) at (?P<time>.+) for the blood test")
def step_impl(context, blood_test_location, date, time):
    """
    :type context: behave.runner.Context
    :type blood_test_location: str
    :type date: str
    :type time: str
    """
    record = base.my_db[BloodTest.__name__].insert_one(
        {
            "purpose": context.blood_test_purpose,
            "location": blood_test_location,
            "date": date,
            "time": time,
            "doctor_id": context.doctor.id_cart,
            "patient_id": context.patient.id_cart,
        }
    )

    context.blood_test = BloodTest(
        blood_test_id=record.inserted_id,
        purpose=context.blood_test_purpose,
        location=blood_test_location,
        date=date,
        time=time,
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
    )
    record = base.my_db[BloodTest.__name__].find_one({"_id": context.blood_test.blood_test_id})
    assert context.blood_test.blood_test_id == record["_id"]
    assert context.blood_test.purpose == record["purpose"]
    assert context.blood_test.location == record["location"]
    assert context.blood_test.date == record["date"]
    assert context.blood_test.time == record["time"]
    assert context.blood_test.doctor_id == record["doctor_id"]
    assert context.blood_test.patient_id == record["patient_id"]

    log.log.info(f"doctor {context.doctor.name} tells to patient {context.patient.name} to go to {blood_test_location} on {date} at {time} for the blood test")

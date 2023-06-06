__author__ = "Taravat"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "tarvtm@gmail.com"
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


@given("the doctor is logged into the patient (?P<patient_id>.+) record system")
def step_impl(context, patient_id):
    name = names.get_full_name()
    record = base.my_db[Patient.__name__].insert_one({"name": name})
    context.patient = Patient(name=name, id_cart=record.inserted_id )
    context.patient_id = patient_id
    log.log.info(f"the doctor is logged into the patient {patient_id} record system")


@when("they enter new (?P<height>.+)  and (?P<weight>.+) for the patient")
def step_impl(context, height, weight):
    update = context.patient.update_height_weight(context.patient_id,height,weight )
    assert update == True


    log.log.info(f"he enter new height = {height}  and weight = {weight} for the patient")


@then("the system should update the patient record")
def step_impl(context):
    log.log.info(f"the system should update the patient record")




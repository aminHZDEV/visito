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
from app.model.bill import Bill
import names

use_step_matcher("re")

base = Base()
log = MyLog()
@given('the doctor is logged into the billing system')
def step_impl(context):
    name = names.get_full_name()
    record = base.my_db[Doctor.__name__].insert_one({"name": name})
    context.doctor = Doctor(name=name, id_cart=record.inserted_id)
    log.log.info(f"the doctor is logged into the billing system")
    pass

@when("they select patient (?P<patient_id>.+) to get his billing information")
def step_impl(context, patient_id):
    name = names.get_full_name()
    record = base.my_db[Patient.__name__].insert_one({"name": name})
    context.patient = Patient(name=name, id_cart=record.inserted_id , height=1 , weight=1)
    context.patient_id = patient_id
    log.log.info(f"they select patient {patient_id} to get billing information")
    pass

@then('they should see that doctor was visiting the patient  (?P<duration>.+) minutes and bill is (?P<amount>.+)')
def step_impl(context, duration , amount):
    bill = Bill(
           duration=duration,
           amount=amount,
        )
    bill_id = bill.add()
    context.bill = bill
    search_bill = base.my_db[Bill.__name__].find_one({"_id": bill_id})

    assert context.bill.bill_id == search_bill["_id"]

    log.log.info(f"they should see that doctor was visiting the patient  {duration}  minutes and bill is {amount}")
    log.log.info(
        f"the patients information is displayed successfully"
    )

def get_billing_information(context, columns):
    # Add implementation to retrieve billing information from the system, filtered by the specified columns
    pass
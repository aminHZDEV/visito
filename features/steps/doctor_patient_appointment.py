from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.appointment import Appointment
import names

use_step_matcher("re")

base = Base()
log = MyLog()

@step("I create an appointment in (?P<date>.+) and (?P<time>.+) for patient with name (?P<name>.+)")
def step_impl(context, date, time, name):
    base.my_db[Appointment.__name__].insert_one({"name": name, "time": time, "date": date})


@then("an appointment in (?P<date>.+) and (?P<time>.+) for patient with name (?P<name>.+) is saved in database")
def step_impl(context, date, time, name):
    myquery = {"name": name, "date": date, "time": time}
    found = base.my_db[Appointment.__name__].find(myquery)
    assert found is not None
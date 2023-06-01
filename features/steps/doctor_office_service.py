from behave import *

use_step_matcher("re")
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.service import Service
import names

use_step_matcher("re")

base = Base()
log = MyLog()

@when("I add a service (?P<name>.+), (?P<price>.+) and (?P<duration>.+)")
def step_impl(context, name, price, duration):
    """
    :type context: behave.runner.Context
    :type name: str
    :type price: str
    :type duration: str
    """
    service = base.my_db[Service.__name__].insert_one({"name": name, "price": price, "duration": duration})
    log.log.info("Service added successfully")


@then("my service list should include (?P<name>.+), (?P<price>.+) and (?P<duration>.+)")
def step_impl(context, name, price, duration):
    """
    :type context: behave.runner.Context
    :type name: str
    :type price: str
    :type duration: str
    """
    myquery = {"name": name, "price": price, "duration": duration}
    found = base.my_db[Service.__name__].find(myquery)
    assert found is not None
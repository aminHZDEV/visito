__author__ = "isaac1998sm"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "isaacsalmanpour@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from app.model.availability import Availability
from utils.my_log import MyLog
from app.db.base import Base


use_step_matcher("re")

base = Base()
log = MyLog()


@when("I enter (?P<start_time>.+) and (?P<end_time>.+)")
def step_impl(context, start_time, end_time):
    """
    :type context: behave.runner.Context
    :type start_time: str
    :type end_time: str
    """
    context.availability = Availability(start=start_time, end=end_time, date=context.date)
    record = base.my_db[Availability.__name__].insert_one({"date": context.date, "start": start_time,
                                                           "end": end_time})


@when("I select a (?P<date>.+) from the calendar")
def step_impl(context, date):
    """
    :type context: behave.runner.Context
    :type date: str
    """
    context.date = date


@then("I should receive a success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    log.log.info(f"availability time set successfully")


@then("my availability calendar should show that date as available from (?P<start_time>.+) to (?P<end_time>.+)")
def step_impl(context, start_time, end_time):
    """
    :type context: behave.runner.Context
    :type start_time: str
    :type end_time: str
    """
    assert end_time == context.availability.end
    assert start_time == context.availability.start
    log.log.info(
        f"The doctor availability for date {context.availability.date} is from {context.availability.start} to {context.availability.end}")

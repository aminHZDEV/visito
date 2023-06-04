__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

import datetime

from behave import given, when, then, step, use_step_matcher

from utils.my_log import MyLog
from app.db.base import Base
from app.model.analytics import Report
from app.model.appointment import Appointment
from app.model.payment import Payment

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given("necessary collections exist")
def step_impl(context):
    appointment = database_handler.my_db[Appointment.__name__]
    payment = database_handler.my_db[Payment.__name__]
    logger.log.info(f'Collections {Appointment.__name__} and {Payment.__name__} exist.')



@step('I am in the "Reports" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You opened the analytics section.')


@when('I select the time period "(?P<time_period>.+)" for which I want to generate a report')
def step_impl(context, time_period):
    """
    :type context: behave.runner.Context
    :type time_period: str
    """
    context.my_report = Report(database=database_handler.my_db, time_period=time_period)
    logger.log.info('Time interval selected successfully.')


@step('I select the type of report "(?P<report_type>.+)" that I want to generate')
def step_impl(context, report_type):
    """
    :type context: behave.runner.Context
    :type report_type: str
    """
    context.my_report.report_type = report_type
    logger.log.info('Report type selected successfully.')

@step('I click on the "Generate" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.generated_result = context.my_report.generate()
    logger.log.info('Report successfully generated!')



@then("a report for the selected time period with the selected report type should be generated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info(f'Your final result is:\n\t{context.generated_result}')

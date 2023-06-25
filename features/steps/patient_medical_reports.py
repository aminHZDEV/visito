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

from app.db.base import Base
from app.model.record import Record
from utils import dummies
from utils.my_log import MyLog
from utils.status import FindStatus, InsertStatus

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given('I have a medical record with token "(?P<token>.+)"')
def step_impl(context, token):
    """
    :type context: behave.runner.Context
    :type token: str
    """
    context.my_records = database_handler.my_db[Record.__name__]
    my_record = Record(token=token)
    if my_record.find_and_update() is FindStatus.RECORD_FOUND:
        logger.log.info('Medical record found.')
    else:
        logger.log.info('Creating a dummy medical record for given private token.')
        my_record.patient = dummies.DUMMY_PATIENT
        my_record.token = token
        my_record.info = "You'll die soon mate"
        my_record.date = datetime.datetime.utcnow().strftime("%Y-%m-%d %I:%M %p")
        if my_record.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
            logger.log.info('Creation successful.')
        else:
            logger.log.error('Could not creat a dummy medical report.')
            raise RuntimeError('Could not creat a dummy medical report.')
    context.my_record = my_record


@when('I open "Medical Records" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You are looking at "Medical Records". Please enter your private token.')


@step("enter my private token")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('Medical record retrieved successfully.')


@then("my medical record should be shown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info(f'Token {context.my_record.token} corresponds to:'
                    f'\n\tPatient name: {context.my_record.patient.name}'
                    f'\n\tDate: {context.my_record.date}'
                    f'\n\tInformation: {context.my_record.info}')

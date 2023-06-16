__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

import names
import random
from behave import given, when, then, step, use_step_matcher

from app.db.base import Base
from app.model.invoice import Invoice
from app.model.patient import Patient
from app.model.payment import Payment
from utils import dummies
from utils.my_log import MyLog
from utils.status import FindStatus, InsertStatus

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given('An invoice "(?P<invoice_number>.+)" exists')
def step_impl(context, invoice_number):
    """
    :type context: behave.runner.Context
    :type invoice_number: str
    """
    my_invoice = Invoice(invoice_number=invoice_number)
    if my_invoice.find_and_update() is FindStatus.NO_RECORDS:
        logger.log.info('Creating a dummy entry for given invoice number.')
        my_invoice = Invoice(patient=dummies.DUMMY_PATIENT,
                             service='Dummy Service',
                             amount=100,
                             invoice_number=invoice_number)
        if my_invoice.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
            logger.log.info(f'Dummy invoice {invoice_number} created successfully!')
        else:
            logger.log.error('Dummy service creation failed')
    context.my_invoice = my_invoice


@when('I click on its "Pay" option')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('*Payment page opens*')
    logger.log.info('Please enter the amount of money you want to lose :P')


@step("I enter the (?P<amount>.+) of money I want to pay")
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    :type amount: str
    """
    context.my_payment = Payment(amount=int(amount), invoice_number=context.my_invoice.invoice_number)
    logger.log.info(f'You are paying {amount} for {context.my_invoice.invoice_number}')


@step('paid the amount in a certain "(?P<time>.+)"')
def step_impl(context, time):
    """
    :type context: behave.runner.Context
    :type time: str
    """
    context.my_payment.date = time
    logger.log.info(f'Payment finalized at "{time}"')


@then("A payment record should be created documenting my payment")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.my_payment.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
        logger.log.info('Payment record created successfully.')
    else:
        logger.log.error('Payment record creation failed.')
    context.my_invoice.add_payment(context.my_payment)
    if context.my_invoice.add(update=True) is InsertStatus.UPDATED_SUCCESSFULLY:
        logger.log.info(f'Added new payment for invoice {context.my_invoice.invoice_number}.')
    else:
        logger.log.error('Something went wrong while we were trying to'
                         f' add a payment record to {context.my_invoice.invoice_number}')

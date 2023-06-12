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
        dummy = Patient.make_dummy()
        if dummy.find_and_update() is FindStatus.NO_RECORDS:
            if not context.my_patient.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
                logger.log.error(f'Something weird happened while trying to create an entry for {dummy.name}')

        invoice_record = database_handler.my_db[Invoice.__name__].insert_one({
            'patient_id': dummy.id_cart,
            'service': 'Dummy Service',
            'amount': 100,
            'payments': [],
            'invoice_number': invoice_number})
        invoice_record = database_handler.my_db[Invoice.__name__].find_one({'_id': invoice_record.inserted_id})
    context.my_invoice = invoice_record
    context.my_token = invoice_record['invoice_number']
    logger.log.info(f'Invoice {invoice_number} found.')


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
    context.my_amount = int(amount)
    logger.log.info(f'You are paying {amount} for {context.my_token}')


@step('paid the amount in a certain "(?P<time>.+)"')
def step_impl(context, time):
    """
    :type context: behave.runner.Context
    :type time: str
    """
    context.my_time = time
    logger.log.info(f'Payment finalized at "{time}"')


@then("A payment record should be created documenting my payment")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    payment = Payment(amount=context.my_amount,
                      invoice_number=context.my_invoice['invoice_number'],
                      date=context.my_time)
    payment_record = database_handler.my_db[Payment.__name__].insert_one({
        'amount': payment.amount,
        'invoice_number': payment.invoice_number,
        'date': payment.date
    })
    payment.id_cart = payment_record.inserted_id
    database_handler.my_db[Invoice.__name__].update_one({'invoice_number': context.my_token},
                                                        {'$push': {'payments': payment.id_cart}})
    logger.log.info(f'Successfully created a payment entry for {payment.invoice_number}')

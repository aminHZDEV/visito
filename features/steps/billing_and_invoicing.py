__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

from behave import given, when, then, step, use_step_matcher

from app.db.base import Base
from app.model.invoice import Invoice
from app.model.patient import Patient
from utils import dummies
from utils.my_log import MyLog
from utils.status import FindStatus, InsertStatus

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@step('I am in the "Patients" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_invoices = database_handler.my_db[Invoice.__name__]
    logger.log.info('You opened the patients section.')
    logger.log.info('A list of patients is shown.')


@given('A patient under certain "(?P<patient_name>.+)", "(?P<patient_ssid>.+)" exists')
def step_impl(context, patient_name, patient_ssid):
    """
    :type context: behave.runner.Context
    :type patient_name: str
    :type patient_ssid: str
    """
    context.my_patient = Patient(name=patient_name, ssid=patient_ssid)
    if context.my_patient.find_and_update() is FindStatus.RECORD_FOUND:
        logger.log.info(f'Patient record for {patient_name} found.')
    elif context.my_patient.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
        logger.log.info(f'Patient record for {patient_name} created.')
    else:
        logger.log.error(f'Something weird happened while trying to get the entry for {patient_name}')
    logger.log.info(f'A patient named {patient_name} with SSID {patient_ssid} Exists.')


@when("I select that patient to fill out an invoice for them")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_invoice = Invoice(patient=context.my_patient)
    logger.log.info(f'Initializing an invoice for patient {context.my_patient.name}.')


@step('I select the services provided "(?P<services_provided>.+)" to the patient')
def step_impl(context, services_provided):
    """
    :type context: behave.runner.Context
    :type services_provided: str
    """
    context.my_invoice.service = services_provided
    logger.log.info(f'Updated invoice with service information. Patient received {services_provided}.')


@step('I enter the amount "(?P<amount>.+)" for each service provided')
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    :type amount: str
    """
    context.my_invoice.amount = amount
    logger.log.info(f'Updated service amount to {amount}.')


@step('I click on the "Generate Invoice" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_invoice.invoice_number = f'INV-{context.my_invoices.estimated_document_count():04d}'
    if context.my_invoice.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
        logger.log.info(f'Finalized invoice "{context.my_invoice.invoice_number}" and added to collection.')


@then("an invoice should be generated for the selected patient")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_invoices.find_one({'_id': context.my_invoice.id_cart})
    assert context.my_invoice.patient.id_cart == current_record["patient_id"]
    assert context.my_invoice.service == current_record["service"]
    assert context.my_invoice.amount == current_record["amount"]
    assert context.my_invoice.invoice_number == current_record["invoice_number"]
    logger.log.info(f'An invoice with following information created successfully:\n'
                    f'\tInvoice Number: {context.my_invoice.invoice_number}\n'
                    f'\tPatient: {context.my_invoice.patient.name}\n'
                    f'\tService: {context.my_invoice.service}\n'
                    f'\tAmount: {context.my_invoice.amount}')


@given('An Invoice with invoice number "(?P<invoice_number>.+)" exists')
def step_impl(context, invoice_number):
    """
    :type context: behave.runner.Context
    :type invoice_number: str
    """
    my_invoice = Invoice(invoice_number=invoice_number)
    if not (my_invoice.find_and_update() is FindStatus.RECORD_FOUND):
        logger.log.info('Creating a dummy entry for given invoice number.')
        my_invoice = Invoice(dummies.DUMMY_PATIENT,
                             'Dummy Service',
                             amount=100,
                             invoice_number=invoice_number)
        if my_invoice.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
            logger.log.info('Creation successful.')
        else:
            logger.log.error('Could not creat a dummy invoice.')
            raise RuntimeError('Could not creat a dummy invoice.')
    context.my_invoice = my_invoice
    logger.log.info(f'An entry for {invoice_number} exists.')


@when("I select that invoice entry")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info(f'Invoice {context.my_invoice.invoice_number} selected.')


@step('I click on the "Track Payments" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_payments = context.my_invoice.payments
    logger.log.info(f'Payment information for {context.my_invoice.invoice_number} found.')


@then("payments made by the patient should be displayed for the selected invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.my_payments:
        table = '\t|            Date            |     Amount     |'
        for item in context.my_payments:
            table += f'\n\t|{item.date:    %Y-%m-%d %I:%M %p     }|{item.amount: ^16}|'
        logger.log.info(f'List of payments made by {context.my_invoice.patient.name} '
                        f'for {context.my_invoice.invoice_number}:'
                        f'\n{table}')
    else:
        logger.log.info(f'There are no payment records for patient {context.my_invoice.patient.name}.')

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
from app.model.payment import Payment
from utils.my_log import MyLog

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
    patient_record = database_handler.my_db[Patient.__name__].find_one({'name': patient_name,
                                                                        'ssid': patient_ssid})
    if not patient_record:
        patient_record = database_handler.my_db[Patient.__name__].insert_one({'name': patient_name,
                                                                              'ssid': patient_ssid})
        patient_record = database_handler.my_db[Patient.__name__].find_one({'_id': patient_record.inserted_id})
    context.my_patient = Patient(name=patient_record['name'],
                                 ssid=patient_record['ssid'],
                                 id_cart=patient_record['_id'])

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
    current_record = context.my_invoices.insert_one({'patient_id': context.my_invoice.patient.id_cart,
                                                     'service': context.my_invoice.service,
                                                     'amount': context.my_invoice.amount,
                                                     'payments': context.my_invoice.payments,
                                                     'invoice_number': context.my_invoice.invoice_number})
    context.my_invoice.id_cart = current_record.inserted_id
    context.my_record = current_record
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
    invoice_record = context.my_invoices.find_one({'invoice_number': invoice_number})
    if invoice_record is None:
        logger.log.info('Creating a dummy entry for given invoice number.')
        dummy = Patient.make_dummy()
        patient_record = database_handler.my_db[Patient.__name__].find_one({'name': dummy.name,
                                                                            'ssid': dummy.ssid})
        patient_id = None
        if patient_record:
            patient_id = patient_record['_id']
        else:
            patient_id = database_handler.my_db[Patient.__name__].insert_one({'name': dummy.name, 'ssid': dummy.ssid}) \
                .inserted_id
        invoice_record = context.my_invoices.insert_one({
            'patient_id': patient_id,
            'service': 'Dummy Service',
            'amount': 100,
            'payments': [],
            'invoice_number': invoice_number})
        invoice_record = context.my_invoices.find_one({'_id': invoice_record.inserted_id})
    context.my_invoice = invoice_record
    logger.log.info(f'An entry for {invoice_number} exists.')


@when("I select that invoice entry")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info(f'Invoice {context.my_invoice["invoice_number"]} selected.')


@step('I click on the "Track Payments" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_payments = context.my_invoice['payments']
    logger.log.info(f'Payment information for {context.my_invoice["invoice_number"]} found.')


@then("payments made by the patient should be displayed for the selected invoice")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    patient_record = database_handler.my_db[Patient.__name__].find_one({'_id': context.my_invoice["patient_id"]})
    if context.my_payments:
        table = '\t|            Date            |     Amount     |'
        for item in context.my_payments:
            current_payment = database_handler.my_db[Payment.__name__].find_one({'_id': item})
            table += f'\n\t|{current_payment["date"]:    %Y-%m-%d %I:%M %p     }|{current_payment["amount"]: ^16}|'
        logger.log.info(f'List of payments made by {patient_record["name"]} for {context.my_invoice["invoice_number"]}:'
                        f'\n{table}')
    else:
        logger.log.info(f'There are no payment records for patient {patient_record["name"]}.')

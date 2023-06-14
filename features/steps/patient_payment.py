__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import names
from behave import when, then, use_step_matcher, given
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.clinic import Clinic
from app.model.bank import Bank
from app.model.offer import Offer
from app.model.email import Email
from app.model.sms import SMS
from app.model.print import Print
from unittest.mock import Mock, patch


use_step_matcher("re")

base = Base()
log = MyLog()


@given("the patient has a (?P<reason>.+) to see the doctor")
def step_impl(context, reason):
    name = names.get_full_name()
    context.patient = Patient(name=name, reason=reason, phonenumber="0911111111111")


@given("the patient has a (?P<payment_method>.+)")
def step_impl(context, payment_method):
    context.patient.payment_method = payment_method
    id_cart = context.patient.add()
    assert id_cart != -1
    context.patient.id_cart = id_cart
    context.bank = Bank(name="MY BANK", email="MYEMAIL@HOST.COM", number="0210000000")


@when("the patient calls the clinic to book an appointment")
def step_impl(context):
    context.clinic = Clinic(name="MY CLINIC")


@then("the clinic should offer the patient a (?P<time_slot>.+) on a (?P<date>.+)")
def step_impl(context, time_slot, date):
    context.offer = Offer(
        clinic=context.clinic, patient=context.patient, time_slot=time_slot, date=date
    )


@then("the patient should confirm or decline the offer")
def step_impl(context):
    mock_offer = Mock()
    mock_offer.confirm.return_value = True
    patcher = patch.object(context, "offer", mock_offer)
    patcher.start()
    context.patchers.append(patcher)
    context.confirm_status = context.offer.confirm()


@then("the patient should pay (?P<amount>.+) for the appointment")
def step_impl(context, amount):
    assert context.confirm_status
    assert context.offer.appointment(payment=amount) != -1


@then("the clinic should send a (?P<confirmation>.+) to the patient and the bank")
def step_impl(context, confirmation):
    if confirmation == "SMS":
        sms = SMS(number=context.patient.phonenumber)
        assert context.patient.send(
            entity=sms,
            message=f"to patient {context.patient.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )
        sms = SMS(number=context.bank.number)
        assert context.bank.send(
            entity=sms,
            message=f"to bank {context.bank.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )
    elif confirmation == "email":
        email = Email(email=context.patient.email)
        assert context.patient.send(
            entity=email,
            message=f"to patient {context.patient.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )
        email = Email(email=context.bank.email)
        assert context.bank.send(
            entity=email,
            message=f"to bank {context.bank.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )
    elif confirmation == "print":
        print_to_endpoint = Print()
        assert context.patient.send(
            entity=print_to_endpoint,
            message=f"to patient {context.patient.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )
        assert context.bank.send(
            entity=print_to_endpoint,
            message=f"to bank {context.bank.name} pay {context.offer.payment} at {context.offer.time_slot} {context.offer.date}",
        )

    else:
        raise Exception("Unknown method to call bank and patient")

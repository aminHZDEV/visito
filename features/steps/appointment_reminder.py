__author__ = "Hatam"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "hatamabolghasemi@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.reminder import Reminder
import names

use_step_matcher("re")

base = Base()
log = MyLog()

@given('the system wants to send an appointment reminder')
def step_system_wants_to_send_appointment_reminder(context):
    # Perform necessary actions here
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    log.log.info(f"the doctor examines the patient")

@given('the system has (?P<appointment_details>.+)')
def step_system_has_appointment_details(context, appointment_details):
    # Retrieve the appointment details and perform necessary actions here
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    context.appointment_details = appointment_details
    log.log.info(f"the system has {appointment_details}")

@when('the system generates an appointment reminder message')
def step_system_generates_appointment_reminder_message(context):
    # Generate the appointment reminder message and perform necessary actions here
    log.log.info(f"the system generates an appointment reminder message")

@then("the system should send the message to the patient's (?P<contact_details>.+)")
def step_system_sends_message_to_patient_contact_details(context, contact_details):
    # Retrieve the patient's contact details and send the appointment reminder message
    context.contact_details = contact_details
    reminder = Reminder(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        appointment_details=context.appointment_details,
        contact_details=context.contact_details,
    )
    reminder_id = reminder.add()
    context.reminder = reminder
    search_reminder = base.my_db[Reminder.__name__].find_one({"_id": reminder_id})
    assert context.reminder.reminder_id == search_reminder["_id"]
    assert context.reminder.doctor_id == search_reminder["doctor_id"]
    assert context.reminder.patient_id == search_reminder["patient_id"]
    assert context.reminder.appointment_details == search_reminder["appointment_details"]
    assert context.reminder.contact_details == search_reminder["contact_details"]
    log.log.info(f"the system should send the message to the patient's {contact_details}")

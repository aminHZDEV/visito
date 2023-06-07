__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["Kaveh Teymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "sm_roudaki@comp.iust.ac.ir"
__status__ = "Production"

import names
import random
from behave import given, when, then, step, use_step_matcher

from app.db.base import Base
from app.model.appointment import Appointment
from app.model.doctor import Doctor
from app.model.patient import Patient
from utils.my_log import MyLog

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given("I am logged in as an administrator")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You are logged in as an administrator!')


@step('I am in the "Appointment Scheduling" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_appointments = database_handler.my_db[Appointment.__name__]
    logger.log.info('You are inside "Appointment Scheduling" tab.')


@when('I enter the patient "(?P<patient_name>.+)", "(?P<patient_ssid>.+)" for whom I want to schedule an appointment')
def step_impl(context, patient_name, patient_ssid):
    """
    :type context: behave.runner.Context
    :type patient_name: str
    :type patient_ssid: str
    """
    patient_record = database_handler.my_db[Patient.__name__].find_one({'name': patient_name,
                                                                        'ssid': patient_ssid})
    if patient_record:
        context.my_patient = Patient(name=patient_record['name'],
                                     ssid=patient_record['ssid'],
                                     id_cart=patient_record['_id'])
        logger.log.info(f'Patient record for {patient_name} found.')
    else:
        patient_record = database_handler.my_db[Patient.__name__].insert_one({'name': patient_name,
                                                                              'ssid': patient_ssid})
        context.my_patient = Patient(name=patient_name,
                                     ssid=patient_ssid,
                                     id_cart=patient_record.inserted_id)
        logger.log.info(f'Patient record for {patient_name} created.')
    context.my_appointment = Appointment(patient=context.my_patient)


@step('I enter the date and time "(?P<date_and_time>.+)" for the appointment')
def step_impl(context, date_and_time):
    """
    :type context: behave.runner.Context
    :type date_and_time: str
    """
    context.my_appointment.date = date_and_time
    logger.log.info(f'You are setting an appointment for {date_and_time}')


@step('I enter the doctor "(?P<doctor_name>.+)" for the appointment')
def step_impl(context, doctor_name):
    """
    :type context: behave.runner.Context
    :type doctor_name: str
    """
    doctor_record = database_handler.my_db[Doctor.__name__].find_one({'name': doctor_name})
    if doctor_record:
        context.my_doctor = Doctor(name=doctor_record['name'],
                                   gmc_number=doctor_record['gmc_number'],
                                   field=doctor_record['field'],
                                   id_cart=doctor_record['_id'])
        logger.log.info(f'Doctor record for {doctor_name} found.')
    else:
        name = doctor_name
        field = 'Unknown'
        gmc_number = 'D' + str(random.randint(1, 9999999)).zfill(7)
        doctor_record = database_handler.my_db[Doctor.__name__].insert_one({'name': name,
                                                                            'gmc_number': gmc_number,
                                                                            'field': field})
        context.my_doctor = Doctor(name=doctor_name,
                                   gmc_number=gmc_number,
                                   field=field,
                                   id_cart=doctor_record.inserted_id)
        logger.log.warn(f'Doctor record for {doctor_name} created.')

    context.my_appointment.doctor = context.my_doctor


@step('I click on the "Schedule Appointment" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_appointments.find_one({'patient_id': context.my_patient.id_cart,
                                                       'doctor_id': context.my_doctor.id_cart,
                                                       'date': context.my_appointment.date})
    if current_record:
        logger.log.warn('Record already exists.')
    else:
        current_record = context.my_appointments.insert_one({'patient_id': context.my_patient.id_cart,
                                                             'doctor_id': context.my_doctor.id_cart,
                                                             'date': context.my_appointment.date})
        logger.log.info('Successfully generated a new appointment record.')

    context.my_record = current_record
    context.my_appointment.id_cart = current_record.inserted_id


@then(
    "an appointment should be scheduled for the selected patient with the selected doctor on the selected date and time")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_appointments.find_one({'_id': context.my_appointment.id_cart})
    assert context.my_patient.id_cart == current_record["patient_id"]
    assert context.my_doctor.id_cart == current_record["doctor_id"]
    assert context.my_appointment.date == current_record["date"]
    logger.log.info(f'An appointment with following information created successfully:\n'
                    f'\tPatient: {context.my_patient.name}\n'
                    f'\tDoctor: {context.my_doctor.name}\n'
                    f'\tDate: {current_record["date"]}')

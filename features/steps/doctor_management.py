__author__ = "Mehdi Roudaki"
__copyright__ = "Copyright 2023"
__credits__ = ["KTeymoury", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "sm_roudaki@comp.iust.ac.ir"
__status__ = "Production"

from behave import given, when, then, step, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.doctor import Doctor
import names

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given("I am logged in as an administrator")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You are logged in as an administrator!')


@step('I am in the "Doctors" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_doctors = database_handler.my_db[Doctor.__name__]
    logger.log.info('You clicked on "Doctors" button.')
    logger.log.info('*shows a list of doctors*')


@when('I click on the "Add Doctor" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You click on "Add" button.')
    logger.log.info('*a pop-up appears asking for administrator information*')


@step("I fill in (?P<doctor_name>.+), (?P<gmc_number>.+), (?P<field>.+) information")
def step_impl(context, doctor_name, gmc_number, field):
    """
    :type context: behave.runner.Context
    :type doctor_name: str
    :type gmc_number: str
    :type field: str
    """
    context.my_doctor = Doctor(name=doctor_name, gmc_number=gmc_number, field=field)
    logger.log.info(f'Information for "{doctor_name}" was entered successfully.')


@step('I click on the "Submit" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_doctors.find_one({'gmc_number': context.my_doctor.gmc_number})
    if current_record:
        if context.my_doctor.name == current_record['name']:
            logger.log.info('Information was already submitted!')
            context.my_doctor.id_cart = current_record['_id']
        else:
            logger.log.error('Failed to create a new entry because a doctor with that GMC number already exists.'
                             'Please use update function to edit existing records.')
    else:
        current_record = context.my_doctors.insert_one(
            {'name': context.my_doctor.name,
             'gmc_number': context.my_doctor.gmc_number,
             'field': context.my_doctor.field})
        context.my_doctor.id_cart = current_record.inserted_id
        context.my_record = current_record
        logger.log.info('Information submitted successfully!')


@then('the entry should be added to the "Doctor" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.my_doctor.id_cart:
        current_record = context.my_doctors.find_one(
            {"_id": context.my_doctor.id_cart})
        assert context.my_doctor.id_cart == current_record["_id"]
        assert context.my_doctor.name == current_record["name"]
        assert context.my_doctor.gmc_number == current_record["gmc_number"]
        assert context.my_doctor.field == current_record["field"]

        logger.log.info(f'Successfully created an entry for {current_record["name"]}.\n'
                        f'\tGMC Number: {current_record["gmc_number"]}\n'
                        f'\tField: {current_record["field"]}')
    else:
        logger.log.error(f'Failed to create a new entry for Dr. {context.my_doctor.name}')


@when("I look at the existing entries")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('*You look at the shown list*')


@then("I should be able to see a table of existing doctors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    table = '\t|      Doctor Name      |   GMC Number   |        Field        |'
    for item in context.my_doctors.find({}):
        table += f'\n\t|{item["name"]: ^23}|{item["gmc_number"]: ^16}|{item["field"]: ^21}|'

    logger.log.info(f'A list of existing admins is shown:\n{table}')


@given("a doctor with GMC number (?P<gmc_number>.+) exists")
def step_impl(context, gmc_number):
    """
    :type context: behave.runner.Context
    :type gmc_number: str
    """
    current_record = context.my_doctors.find_one({'gmc_number': gmc_number})
    if current_record:
        context.target_id = current_record['_id']
    else:
        name = names.get_full_name()
        field = 'Unknown'
        current_record = context.my_doctors.insert_one(
            {'name': name, 'gmc_number': gmc_number, 'field': field})
        context.target_id = current_record.inserted_id
    context.my_doctor = Doctor(name=current_record['name'],
                               gmc_number=current_record['gmc_number'],
                               field=current_record['field'],
                               id_cart=current_record['_id'])
    logger.log.info(f'A doctor with GMC number {gmc_number} is selected')


@when("I edit (?P<doctor_name>.+), (?P<field>.+) information of that doctor")
def step_impl(context, doctor_name, field):
    """
    :type context: behave.runner.Context
    :type doctor_name: str
    :type field: str
    """
    context.my_doctor.name = doctor_name
    context.my_doctor.field = field
    logger.log.info(f'You updated the fields with following information '
                    f'[name: {doctor_name} | field: {field}]')


@step('I click on the "Update" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_doctors.update_one(
        {'_id': context.target_id},
        {'$set': {'name': context.my_doctor.name, 'field': context.my_doctor.field}}
    )
    logger.log.info('Update was successful!')


@then('the entry should be updated in the "Doctor" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_doctors.find_one({"_id": context.target_id})
    assert context.my_doctor.id_cart == current_record["_id"]
    assert context.my_doctor.name == current_record["name"]
    assert context.my_doctor.gmc_number == current_record["gmc_number"]
    assert context.my_doctor.field == current_record["field"]
    logger.log.info(f'Successfully updated the following doctor\'s information:\n'
                    f'\tGMC Number: {current_record["gmc_number"]}\n'
                    f'\tFull Name: {current_record["name"]}\n'
                    f'\tField: {current_record["field"]}')


@when('I click on the "Delete" button of that doctor entry')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_doctors.delete_one({'_id': context.target_id})
    logger.log.info('Deletion was successful!')


@then('the entry should be deleted from the "Doctor" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_doctors.find_one({"_id": context.target_id})
    if current_record:
        logger.log.error(f'Doctor {context.my_doctors.name} still remains in the collection!')
    else:
        logger.log.info(f'Doctor {context.my_doctors.name} has been successfully removed from the collection!')

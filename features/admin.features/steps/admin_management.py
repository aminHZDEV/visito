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
from app.model.administrator import Administrator
import names
import random

from utils.status import InsertStatus, FindStatus

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@given("I am logged in as an administrator")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You are logged in as an administrator!')


@step('I am in the "Admins" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_administrators = database_handler.my_db[Administrator.__name__]
    logger.log.info('You clicked on "Admins" button.')
    logger.log.info('*shows a list of administrators*')


@when('I click on the "Add Admin" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('You click on "Add" button.')
    logger.log.info('*a pop-up appears asking for administrator information*')


@step("I fill in (?P<administrator_name>.+), (?P<username>.+), (?P<password>.+) information")
def step_impl(context, administrator_name: str, username: str, password: str):
    """
    :type context: behave.runner.Context
    :type administrator_name: str
    :type username: str
    :type password: str
    """
    context.my_admin = Administrator(name=administrator_name, username=username, password=password)
    logger.log.info(f'Information for "{administrator_name}" was entered successfully.')


@step('I click on the "Submit" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_administrators.find_one({'username': context.my_admin.username})
    if current_record:
        if context.my_admin.name == current_record['name']:
            logger.log.info('Information was already submitted!')
            context.my_admin.id_cart = current_record['_id']
        else:
            logger.log.error('Failed to create a new entry because username was taken by someone else.')
    else:
        if context.my_admin.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
            logger.log.info('Information submitted successfully!')
        else:
            logger.log.info('Information submission failed!')


@then('the entry should be added to the "Admin" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.my_admin.id_cart:
        current_record = context.my_administrators.find_one(
            {"_id": context.my_admin.id_cart})
        assert context.my_admin.id_cart == current_record["_id"]
        assert context.my_admin.name == current_record["name"]
        assert context.my_admin.username == current_record["username"]
        assert context.my_admin.password == current_record["password"]

        logger.log.info(f'Successfully created an entry for {current_record["name"]}.\n'
                        f'\tUsername: {current_record["username"]}\n'
                        f'\tPassword: {current_record["password"]}')
    else:
        logger.log.error(f'Failed to create a new entry for {context.my_admin.name}')


@when("I look at the existing entries")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('*You look at the shown list*')


@then("I should be able to see a table of existing administrators")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    table = '\t|   Administrator Name   |   Username   |   Password   |'
    for item in context.my_administrators.find({}):
        table += f'\n\t|{item["name"]: ^24}|{item["username"]: ^14}|{item["password"]: ^14}|'

    logger.log.info(f'A list of existing admins is shown:\n{table}')


@given("an admin with username (?P<username>.+) exists")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    my_admin = Administrator(username=username)
    if not (my_admin.find_and_update() is FindStatus.RECORD_FOUND):
        my_admin.name = names.get_full_name()
        my_admin.password = random.randint(1000, 99999999)
        my_admin.add(update=False)
    context.my_admin = my_admin
    logger.log.info(f'Username {username} belonging to {my_admin.name} is selected')


@when("I edit (?P<administrator_name>.+), (?P<password>.+) information of that administrator entry")
def step_impl(context, administrator_name, password):
    """
    :type context: behave.runner.Context
    :type administrator_name: str
    :type password: str
    """
    context.my_admin.name = administrator_name
    context.my_admin.password = password
    logger.log.info(f'You updated the fields with following information '
                    f'[name: {administrator_name} | password: {password}]')


@step('I click on the "Update" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.my_admin.add(update=True) is InsertStatus.UPDATED_SUCCESSFULLY:
        logger.log.info('Update was successful!')
    else:
        logger.log.info('Failed to update entry!')



@then('the entry should be updated in the "Admin" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_administrators.find_one({"_id": context.my_admin.id_cart})
    assert context.my_admin.id_cart == current_record["_id"]
    assert context.my_admin.name == current_record["name"]
    assert context.my_admin.username == current_record["username"]
    assert context.my_admin.password == current_record["password"]
    logger.log.info(f'Successfully updated the following user\'s information:\n'
                    f'\tUsername: {current_record["username"]}\n'
                    f'\tFull Name: {current_record["name"]}\n'
                    f'\tPassword: {current_record["password"]}')


@when('I click on the "Delete" button of that administrator entry')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_administrators.delete_one({'_id': context.my_admin.id_cart})
    logger.log.info('Deletion was successful!')


@then('the entry should be deleted from the "Admin" collection')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_administrators.find_one({"_id": context.my_admin.id_cart})
    if current_record:
        logger.log.error(f'User {context.my_admin.username} still remains in the collection!')
    else:
        logger.log.info(f'User {context.my_admin.username} has been successfully removed from the collection!')

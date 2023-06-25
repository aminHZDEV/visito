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
from app.model.medicine import Medicine
from utils.my_log import MyLog
from utils.status import FindStatus, InsertStatus

use_step_matcher("re")

database_handler = Base()
logger = MyLog()


@step('I am in the "Inventory" section')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_inventory = database_handler.my_db[Medicine.__name__]
    logger.log.info('You clicked on "Inventory" button.')
    logger.log.info('*shows a list of medications*')


@when('I enter the item "(?P<item_name>.+)" that I want to add to inventory')
def step_impl(context, item_name):
    """
    :type context: behave.runner.Context
    :type item_name: str
    """
    my_medicine = Medicine(name=item_name)
    if my_medicine.find_and_update() is FindStatus.RECORD_FOUND:
        context.already_exists = True
        logger.log.info(f'An entry for {item_name} found.')
    else:
        context.already_exists = False
        logger.log.info(f'A new entry for {item_name} will be created.')
    context.my_medicine = my_medicine


@step('I enter the quantity "(?P<quantity>.+)" of the item that I want to add to inventory')
def step_impl(context, quantity):
    """
    :type context: behave.runner.Context
    :type quantity: str
    """
    context.my_medicine.increase_quantity(int(quantity))
    logger.log.info(f'Added {quantity} items. total: {context.my_medicine.quantity}.')


@step('I click on the "Add Item" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.already_exists:
        if context.my_medicine.add(update=True) is InsertStatus.UPDATED_SUCCESSFULLY:
            logger.log.info('Item Updated in inventory.')
        else:
            logger.log.warn("Couldn't update the item's record.")
    else:
        if context.my_medicine.add(update=False) is InsertStatus.INSERTED_SUCCESSFULLY:
            logger.log.info('Item added to inventory.')
        else:
            logger.log.warn("Couldn't add the item.")


@then("the item should be added to the inventory")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    current_record = context.my_inventory.find_one({"_id": context.my_medicine.id_cart})
    assert context.my_medicine.id_cart == current_record["_id"]
    assert context.my_medicine.name == current_record["name"]
    assert context.my_medicine.quantity == current_record["quantity"]

    logger.log.info(f'Successfully updated inventory entry for {current_record["name"]}.\n'
                    f'\tQuantity: {current_record["quantity"]}')


@when("I look at the existing medications")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.log.info('*You look at the shown list*')


@then("I should be able to see a table of existing medications")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    table = '\t|      Item Name      |  Quantity  |'
    for item in context.my_inventory.find({}):
        table += f'\n\t|{item["name"]: ^21}|{item["quantity"]: ^12}|'
    logger.log.info(f'A list of existing medications is shown:\n{table}')


@given('An entry for "(?P<item_name>.+)" exists')
def step_impl(context, item_name):
    """
    :type context: behave.runner.Context
    :type item_name: str
    """
    current_record = context.my_inventory.find_one({'name': item_name})
    if current_record:
        context.target_id = current_record['_id']
        logger.log.info(f'Found an entry for {item_name}.')
    else:
        current_record = context.my_inventory.insert_one({'name': item_name,
                                                          'quantity': 0})
        context.target_id = current_record.inserted_id
        logger.log.info(f'Temporarily created a new entry for {item_name}.')


@when('I click on the "Remove Item" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.my_inventory.delete_one({'_id': context.target_id})
    logger.log.info('Removed an item from inventory!')


@then("the item should be removed from the inventory")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.my_inventory.find_one({'_id': context.target_id}) is None
    logger.log.info('Removal was successful.')

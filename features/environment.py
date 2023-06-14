__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

from utils.decorators.behave_examples_decorator import insert_examples


@insert_examples()
def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context.patchers = []


def before_step(context, step):
    pass


def before_tag(context, tag):
    pass


def before_all(context):
    pass


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    for patcher in context.patchers:
        patcher.stop()


def after_step(context, step):
    pass


def after_tag(context, tag):
    pass


def after_all(context):
    pass

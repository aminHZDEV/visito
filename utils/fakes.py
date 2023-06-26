__author__ = "KTeymoury"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Hamid Moradi"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "kaveh.teymoury@gmail.com"
__status__ = "Production"

import warnings

import mongomock
from _pytest.monkeypatch import MonkeyPatch
from bson.json_util import loads

from app.db.base import Base

__first_time = True
__is_initiated = False
__monkey = MonkeyPatch()

FAKE_CLIENT = None
FAKE_DB = None


def __initiate():
    global FAKE_CLIENT
    global FAKE_DB
    global __is_initiated
    if __is_initiated:
        warnings.warn('Re initiating an already initiated mongomock instance!')
    FAKE_CLIENT = mongomock.MongoClient()
    FAKE_DB = FAKE_CLIENT['Test']
    __is_initiated = True


def __fill_database(path: str = '../resources/default_database/'):
    global FAKE_CLIENT
    global FAKE_DB
    if not __is_initiated:
        raise RuntimeError('You must initiate your mock database before filling it mate.')
    if not (path[-1] == '/' or path[-1] == '\\'):
        path += '/'
    for collection in ['Administrator', 'Patient', 'Doctor', 'Medicine', 'Payment', 'Record', 'Invoice', 'Appointment']:
        with open(f'{path}{collection}.json', 'r', encoding='UTF-8') as f:
            FAKE_DB[collection].insert_many(loads(f.read()))


def __fake_init(self):
    super(Base, self).__init__()
    self._mongo_client = FAKE_CLIENT
    self._my_db = FAKE_DB


def patch_base():
    if not __is_initiated:
        raise RuntimeError('You must initiate your mock database before patching.')
    global __monkey
    __monkey.setattr('app.db.base.Base.__init__', __fake_init)


if __first_time:
    __initiate()
    __fill_database()
    __first_time = False

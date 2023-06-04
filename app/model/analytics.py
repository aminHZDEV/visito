__author__ = "Hamid Moradi Kamali"
__copyright__ = "Copyright 2023"
__credits__ = ["Mehdi Roudaki", "Kaveh Teymori"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "hordimad21@gmail.com"
__status__ = "Production"

import datetime
from pymongo.database import Database

from app.model.appointment import Appointment
from app.model.payment import Payment


def _visit_report(database: Database, begin_date: datetime.datetime, end_date: datetime.datetime) -> str:
    visit_count = database[Appointment.__name__].count_documents({"date": {"$lte": end_date, '$gte': begin_date}})
    return f'Total number of patient visits from {begin_date:%Y-%m-%d} to {end_date:%Y-%m-%d} is: {visit_count}'


def _revenue_report(database: Database, begin_date, end_date) -> str:
    revenue = 0
    for item in database[Payment.__name__].find({"date": {"$lte": end_date, '$gte': begin_date}}):
        revenue += item['amount']
    return f'Total income from {begin_date:%Y-%m-%d} to {end_date:%Y-%m-%d} is: {revenue}'


_report_functions = {'Patient Visits': _visit_report,
                     'Revenue': _revenue_report,
                     'NOP': None}


class Report:
    def __init__(self, database: Database = None,  time_period: str = "1990-01-01 to 2023-12-20", report_type: str = "NOP"):
        self._database = database
        period = time_period.split(' to ')
        self._date_from = datetime.datetime.strptime(period[0], "%Y-%m-%d")
        self._date_to = datetime.datetime.strptime(period[1], "%Y-%m-%d")
        self._report_type = report_type
        self._report_function = _report_functions[report_type]

    # Setters and Getters lie beyond this comment
    # Report Type/Function Accessor
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, a):
        self._report_type = a
        self._report_function = _report_functions[a]

    # Database accessor
    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, a):
        self._database = a

    # Date accessors
    @property
    def date_from(self):
        return self._date_from

    @property
    def date_to(self):
        return self._date_to

    # Date setter function
    def set_period(self, time_period: str):
        period = time_period.split(' to ')
        self._date_from = datetime.datetime.strptime(period[0], "%Y-%m-%d")
        self._date_to = datetime.datetime.strptime(period[1], "%Y-%m-%d")

    # Report generator
    def generate(self, indent=0) -> str:
        if self._report_function is None:
            raise AttributeError('You need to select a report type first.')
        return self._report_function(self._database, self.date_from, self.date_to)


import pytest

from app.model.analytics import Report
from utils.fakes import FAKE_DB

params = [(Report(database=FAKE_DB, time_period='1990-01-01 to 2023-12-20', report_type='Patient Visits'),
           'Total number of patient visits from 1990-01-01 to 2023-12-20 is: 3'),
          (Report(database=FAKE_DB, time_period='2022-12-01 to 2023-02-01', report_type='Patient Visits'),
           'Total number of patient visits from 2022-12-01 to 2023-02-01 is: 1'),
          (Report(database=FAKE_DB, time_period='2022-12-01 to 2023-06-01', report_type='Patient Visits'),
           'Total number of patient visits from 2022-12-01 to 2023-06-01 is: 2'),
          (Report(database=FAKE_DB, time_period='2022-12-01 to 2023-09-01', report_type='Revenue'),
           'Total income from 2022-12-01 to 2023-09-01 is: 300'),
          (Report(database=FAKE_DB, time_period='2022-12-01 to 2023-03-01', report_type='Revenue'),
           'Total income from 2022-12-01 to 2023-03-01 is: 150'),
          (Report(database=FAKE_DB, time_period='2022-12-01 to 2023-05-02', report_type='Revenue'),
           'Total income from 2022-12-01 to 2023-05-02 is: 250')]


@pytest.mark.parametrize("test_input, expected", params)
def test_report_generation(test_input, expected):
    assert test_input.generate() == expected

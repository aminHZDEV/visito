import pytest
from app.model.availability import Availability
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("doctor_availability.csv")


@pytest.mark.parametrize(titles, testcases)
def test_availability_add(date, expected):
    availability = Availability(start='1', end='1', date=date)
    assert availability.add() != expected
    log.log.info(f"test availability passed. {date} != {expected} as expected\n")

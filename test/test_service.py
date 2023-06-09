import pytest
from app.model.service import Service
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("appointment.csv")


@pytest.mark.parametrize(titles, testcases)
def test_appointment_add(duration, expected):
    service = Service(name='1', duration='1', price=duration)
    assert service.add() != expected
    log.log.info(f"test service passed. {duration} != {expected} as expected\n")
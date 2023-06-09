import pytest
from app.model.appointment import Appointment
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("appointment.csv")


@pytest.mark.parametrize(titles, testcases)
def test_appointment_add(date, expected):
    appointment = Appointment(name='1', time='1', date=date)
    assert appointment.add() != expected
    log.log.info(f"test appointment passed. {date} != {expected} as expected\n")
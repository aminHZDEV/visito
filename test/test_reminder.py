import pytest
from app.model.reminder import Reminder
from utils.pytest_parametarize import insert_testcases
from utils.my_log import MyLog

log = MyLog()

titles, testcases = insert_testcases("appointment_reminder.csv")


@pytest.mark.parametrize(titles, testcases)
def test_reminder_add(appointment_details, expected):
    reminder = Reminder(appointment_details=appointment_details)
    assert reminder.add() != expected
    log.log.info(
        f"pytest reminder add function pass name :  {appointment_details} != expected {expected} \n"
    )

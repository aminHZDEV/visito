__author__ = "Hatam"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "hatamabolghasemi@gmail.com"
__status__ = "Production"

from behave import given, when, then, use_step_matcher
from utils.my_log import MyLog
from app.db.base import Base
from app.model.patient import Patient
from app.model.doctor import Doctor
from app.model.test_result import TestResults
import names

use_step_matcher("re")

base = Base()
log = MyLog()


@given("the patient has taken (?P<medical_test>.+)")
def step_impl(context, medical_test):
    name = names.get_full_name()
    patient = Patient(name=name)
    patient.add()
    context.patient = patient
    context.medical_test = medical_test
    log.log.info(f"the patient has taken {medical_test}")


@when("the doctor releases the test results")
def step_impl(context):
    name = names.get_full_name()
    doctor = Doctor(name=name)
    doctor.add()
    context.doctor = doctor
    log.log.info(f"the doctor releases the test results")


@then("the system should display the (?P<results>.+) to the patient")
def step_impl(context, results):
    context.results = results
    test_results = TestResults(
        doctor_id=context.doctor.id_cart,
        patient_id=context.patient.id_cart,
        results=context.results,
        medical_test=context.medical_test,
    )
    test_results_id = test_results.add()
    context.test_results = test_results
    search_test_results = base.my_db[TestResults.__name__].find_one({"_id": test_results_id})
    assert context.test_results.test_result_id == search_test_results["_id"]
    assert context.test_results.doctor_id == search_test_results["doctor_id"]
    assert context.test_results.patient_id == search_test_results["patient_id"]
    assert context.test_results.medical_test == search_test_results["medical_test"]
    assert context.test_results.results == search_test_results["results"]
    log.log.info(f"the system should display the {results} to the patient")

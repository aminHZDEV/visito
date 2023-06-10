# Created by Isaac at ۲۸/۰۵/۲۰۲۳
Feature: blood test order
  As a doctor
  I want to order a blood test for the patient
  So that I can check their blood levels

  Scenario Outline: Doctor orders a blood test for the patient
    Given a patient named <name> who needs a blood test
    When the doctor orders a blood test for the patient
    Then the doctor should inform the patient about the blood test procedure and purpose as checking their <blood_test_purpose>
    And the doctor should tell the patient to go to <blood_test_location> on <date> at <time> for the blood test

    Examples:
      | name   | blood_test_purpose | blood_test_location | date      | time     |
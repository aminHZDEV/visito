# Created by Isaac at ۲۸/۰۵/۲۰۲۳
Feature: blood test review
  As a doctor
  I want to review the blood test results of the patient
  So that I can diagnose and treat them accordingly

  Scenario Outline: Doctor reviews the blood test results of the patient
    Given a patient named <name> who has done a blood test
    When the doctor receives the blood test results from the laboratory as <blood_test_result>
    Then if necessary, prescribe <medication> or further tests for them.

    Examples:
      | name    | blood_test_result     | medication       |
      | Alice   | low iron levels       | iron supplements |
      | Bob     | high allergy levels   | corticosteroids  |
      | Charlie | high infection levels | antibiotics      |



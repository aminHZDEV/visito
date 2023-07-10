# Created by Narges Abbasi
Feature: Lab Test Ordering with Test Types

  Scenario Outline: Order a lab test for a patient
    Given I am a doctor and i want to order a lab test for a patient.
    When I enter the patient's information <patient_name> and the <test_type>
    Then the test should be ordered successfully

    Examples:
      | patient_name | test_type          |
      | John Smith   | complete blood count |
      | Jane Doe     | thyroid function test |
Feature: Patient Medical Reports
  As a patient
  I want to be able to have access to my medical records
  So that I can view test results

  Scenario Outline: Access to medical records
    Given I have a medical record with token "<token>"
    When I open "Medical Records" section
    And enter my private token
    Then my medical record should be shown

    Examples:
      | token     |
      | 123456789 |
      | 987654321 |

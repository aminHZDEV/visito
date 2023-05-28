Feature: Patient Portal
  As a patient
  I want to be able to have access to my medical records
  So that I can view test results

  Scenario Outline: Access to medical records
    Given I am in the "Medical Records" section
    When I enter the recieved <token>
    And I click on the "Show" button
    Then my medical records should be shown

    Examples:
      | token     |
      | 123456789 |
      | 987654321 |

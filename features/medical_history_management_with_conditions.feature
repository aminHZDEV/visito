Feature: Medical History Management with Conditions

  Scenario Outline: Add a medical condition to a patient's record
    Given I am a doctor
    And I want to add a medical condition to a patient's record
    When I enter the patient's information <patient_name> and medical condition <condition>
    Then the condition added successfully

    Examples:
      | patient_name | condition               |
      | John Smith   | High blood pressure     |
      | Jane Doe     | Diabetes type 2         |
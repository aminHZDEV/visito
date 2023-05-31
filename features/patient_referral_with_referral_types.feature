Feature: Patient Referral with Referral Types

  Scenario Outline: Refer a patient to a specialist
    Given I am a doctor
    And I want to refer a patient to a specialist
    When I enter the patient's information<patient_name> and the specialist type<specialist_type>
    Then the referral made successfully

    Examples:
      | patient_name | specialist_type   |
      | John Smith   | cardiologist      |
      | Jane Doe     | dermatologist     |
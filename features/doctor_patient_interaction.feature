Feature: Doctor and Patient Interaction

  Scenario Outline: Doctor visits patient
    Given the patient has <symptom>
    When the doctor examines the patient
    Then the doctor should be able to diagnose <diagnosis>
    And the doctor should prescribe <medicine>

    Examples:
      | symptom      | diagnosis | medicine |
      | headache     | migraine  | aspirin  |
      | stomach ache | gastritis | antacid  |
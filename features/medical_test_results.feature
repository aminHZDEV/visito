Feature: Medical Test Results

  Scenario Outline: Patient receives medical test results
    Given the patient has taken <medical_test>
    When the doctor releases the test results
    Then the system should display the <results> to the patient

    Examples:
    | results              | medical_test  |
    | High Blood Pressure  | blood glucose |
    | High Fat             | cholesterol   |
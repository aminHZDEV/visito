Feature: Medical Test Results

  Scenario Outline: Patient receives medical test results
    Given the patient has taken <medical_test>
    When the doctor releases the test results
    Then the system should display the <results> to the patient

    Examples:
    | results              | medical_test  |
    | Positive for drug abuse | Urine drug test |
    | Abnormal chest X-ray images | Chest X-ray test |
    | Irregular heart rhythm | Electrocardiogram (ECG) test |
    | Elevated blood pressure | Blood pressure test |
    | Low hemoglobin levels | Complete blood count (CBC) test |
    | Positive for COVID-19 | COVID-19 test |
    | High cholesterol levels | Cholesterol test |
    | Abnormal liver function | Liver function test |
    | Underactive thyroid gland | Thyroid function test |
    | Inconclusive mammogram results | Mammogram test |
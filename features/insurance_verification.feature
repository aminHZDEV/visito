Feature: Insurance Verification

  Scenario Outline: Verify patient insurance information
    Given the patient wants to verify their <insurance_information>
    When the <receptionist> enters the patient's insurance information
    Then the system should confirm the insurance details and display the <patient_copay_amount>

    Examples:
    | insurance_information     | receptionist    | patient_copay_amount  |



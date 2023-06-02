Feature: Insurance Verification

  Scenario Outline: Verify patient insurance information
    Given the patient wants to verify their <insurance_information>
    When the <receptionist> enters the patient's insurance information
    Then the system should confirm the insurance details and display the <patient_copay_amount>

    Examples:
    | insurance_information     | receptionist    | patient_copay_amount  |
    | Blue Shield of California | Jessica Nguyen  | $45.00                |
    | Humana                    | Michael Smith   | $30.00                |
    | Kaiser Permanente         | Sarah Patel     | $20.00                |
    | Aetna                     | David Rodriguez | $15.00                |
    | Blue Cross Blue Shield    | John Smith      | $20.00                |
    | Aetna                     | Jane Doe        | $10.00                |
    | United Healthcare         | Bob Johnson     | $5.00                 |
    | Cigna                     | Sarah Thompson  | $15.00                |



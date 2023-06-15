# Created by taravat Monsef
Feature:Calculate Bill
  As a doctor I want to give my patient a bill for him to pay
  So I select a patient and the system should give a bill.

  Scenario Outline: Create a Bill for a Patient Visit
    Given the doctor is logged into the billing system
    When they select patient <patient_id> to get his billing information
    Then they should see that doctor was visiting the patient  <duration> minutes and bill is <amount>


    Examples:
      | patient_id   | duration     | amount   |
      |  1           | 50           | $100.00  |
      |  2           | 30           | $250.00  |
      |  3           | 10           | $75.00   |
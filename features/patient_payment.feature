Feature: Patient takes a turn and requests to bank

  Scenario Outline: Patient makes an appointment and pays for it
    Given the patient has a <reason> to see the doctor
    And the patient has a <payment_method>
    When the patient calls the clinic to book an appointment
    Then the clinic should offer the patient a <time_slot> on a <date>
    And the patient should confirm or decline the offer
    And the patient should pay <amount> for the appointment
    And the clinic should send a <confirmation> to the patient and the bank

    Examples:
      | reason | payment_method | time_slot | date | amount | confirmation |

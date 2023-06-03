Feature: Appointment Reminder

  Scenario Outline: Send appointment reminder to patient
    Given the system wants to send an appointment reminder
    And the system has <appointment_details>
    When the system generates an appointment reminder message
    Then the system should send the message to the patient's <contact_details>

    Examples:
    | appointment_details                                           | contact_details                 |

Feature: Doctor-Patient Interaction
  As a patient
  I want to visit my doctor
  So that I can get medical advice

  Scenario Outline: Schedule an appointment with the doctor
    Given I am on the clinic's website
    When I click on "Schedule an appointment"
    Then I should see "Appointment scheduling form"

    And I fill out the form with:
      | First Name | Last Name | Email Address         | Phone Number | Appointment Date | Appointment Time |
      | <first_name>       | <last_name>       | <email_address>  | <phone_number>   | <appointment_date>       | <appointment_time>         |

    Examples:
      | first_name  | last_name   | email_address          | phone_number   | appointment_date   | appointment_time |
      | John        | Doe         | john.doe@example.com   | 1234567890     | 2023-06-01         | 10:00 AM         |
      | Jane        | Smith       | jane.smith@example.com | 0987654321     | 2023-06-02         | 2:00 PM          |

  Scenario: Fill out appointment form
    Given I am on the "Appointment scheduling form"
    When I fill out the form with my information
    And click on "Submit"
    Then I should see "Appointment confirmation page"

  Scenario: Cancel appointment
    Given I have an upcoming appointment
    When I click on "Cancel appointment"
    Then I should see "Appointment cancellation confirmation page"

  Scenario: Visit the doctor
    Given I have an appointment with Dr. Smith at the clinic on June 1st at 10:00 AM
    When I arrive at the clinic and check in at the front desk
    Then I should be directed to the waiting room

  Scenario: Doctor examines patient
    Given I am in the waiting room
    When Dr. Smith calls my name and takes me to his office
    Then he should ask me about my symptoms

  Scenario: Doctor prescribes medication
    Given Dr. Smith has diagnosed me with a condition that requires medication
    When he prescribes me medication for my condition
    Then he should explain how to take it and any potential side effects

  Scenario: Patient pays for services rendered
    Given Dr. Smith has provided me with medical advice and prescribed medication
    When I go to the front desk to pay for services rendered
    Then they should provide me with a receipt
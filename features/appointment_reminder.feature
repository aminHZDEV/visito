Feature: Appointment Reminder

  Scenario Outline: Send appointment reminder to patient
    Given the system wants to send an appointment reminder
    And the system has <appointment_details>
    When the system generates an appointment reminder message
    Then the system should send the message to the patient's <contact_details>

    Examples:
    | appointment_details                                           | contact_details                 |
    | Dental check-up with Dr. Lee on June 10th at 3pm              | email: mary.smith@example.com   |
    | Physical therapy session with Sarah on June 12th at 10am      | phone: +1 (555) 987-6543        |
    | Appointment with Dr. Johnson on June 15th at 1pm              | text message: +1 (555) 123-4567 |
    | Eye exam with Dr. Chen on July 1st at 9am                     | email: john.doe@example.com     |
    | MRI scan with Dr. Kim on July 5th at 2pm                      | phone: +1 (555) 555-5555        |
    | Annual physical with Dr. Patel on July 12th at 11am           | text message: +1 (555) 123-4567 |
    | Therapy session with John on July 19th at 3pm                 | email: jane.doe@example.com     |
    | Appointment with Dr. Taylor on August 2nd at 10am             | phone: +1 (555) 555-1212        |
    | Dermatology appointment with Dr. Lee on August 5th at 1pm     | text message: +1 (555) 987-6543 |
    | Chiropractic adjustment with Dr. Smith on August 12th at 4pm  | email: joe.smith@example.com    |
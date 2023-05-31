Feature: Appointment Scheduling
  As an administrator
  I want to be able to schedule appointments for patients
  So that I can manage patient appointments more efficiently

  Scenario Outline: Schedule an appointment for a patient
    Given I am logged in as an administrator
    And I am in the "Appointment Scheduling" section
    When I enter the patient "<patient_name>", "<patient_ssid>" for whom I want to schedule an appointment
    And I enter the date and time "<date_and_time>" for the appointment
    And I enter the doctor "<doctor_name>" for the appointment
    And I click on the "Schedule Appointment" button
    Then an appointment should be scheduled for the selected patient with the selected doctor on the selected date and time

    Examples:
      | patient_name | patient_ssid | date_and_time       | doctor_name        |
      | John Doe     | 1234567890   | 2023-06-01 10:00 AM | Richard Goodrich   |
      | Jane Smith   | 9087654321   | 2023-06-02 02:00 PM | Christopher Turner |

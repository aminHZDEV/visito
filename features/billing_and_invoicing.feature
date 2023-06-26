Feature: Billing and Invoicing
  As an administrator
  I want to be able to generate invoices and track payments
  So that I can manage billing and invoicing more efficiently

  Background:
    Given I am logged in as an administrator
    And I am in the "Patients" section

  Scenario Outline: Generate an invoice for a patient
    Given A patient under certain "<patient_name>", "<patient_ssid>" exists
    When I select that patient to fill out an invoice for them
    And I select the services provided "<services_provided>" to the patient
    And I enter the amount "<amount>" for each service provided
    And I click on the "Generate Invoice" button
    Then an invoice should be generated for the selected patient

    Examples:
      | patient_name | patient_ssid | services_provided | amount |
      | John Doe     | 1234567890   | Consultation      | 100    |
      | Jane Smith   | 0987654321   | X-ray             | 50     |

  Scenario Outline: Track payments for an invoice
    Given An Invoice with invoice number "<invoice_number>" exists
    When I select that invoice entry
    And I click on the "Track Payments" button
    Then payments made by the patient should be displayed for the selected invoice

    Examples:
      | invoice_number |
      | INV-0001       |
      | INV-0002       |

Feature: Billing and Invoicing
  As an administrator
  I want to be able to generate invoices and track payments
  So that I can manage billing and invoicing more efficiently

  Scenario Outline: Generate an invoice for a patient
    Given I am logged in as an administrator
    And I am in the "Patient" section
    When I select the patient "<patient_name>" for whom I want to generate an invoice
    And I select the services provided "<services_provided>" to the patient
    And I enter the amount "<amount>" for each service provided
    And I click on the "Generate Invoice" button
    Then an invoice should be generated for the selected patient

    Examples:
      | patient_name | services_provided | amount |
      | John Doe     | Consultation      | 100    |
      | Jane Smith   | X-ray             | 50     |

  Scenario Outline: Track payments for an invoice
    Given I am logged in as an administrator
    And I am in the "Patient" section
    When I select the patient "<patient_name>" for whom I want to track payments
    And I select the invoice "<invoice_number>" for which I want to track payments
    And I click on the "Track Payments" button
    Then payments made by the patient should be displayed for the selected invoice

    Examples:
      | patient_name | invoice_number |
      | John Doe     | INV-001        |
      | Jane Smith   | INV-002        |

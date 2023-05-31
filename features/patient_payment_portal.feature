Feature: Patient Payment Portal
  As a patient
  I want to be able to access my invoices
  So that I can pay my bills in time

  Scenario Outline: Access to medical records
    Given An invoice "<invoice_number>" exists
    When I click on its "Pay" option
    And I enter the <amount> of money I want to pay
    Then A payment record should be created documenting my payment

    Examples:
      | invoice_number | amount |
      | INV-0001       | 50     |
      | INV-0002       | 05     |

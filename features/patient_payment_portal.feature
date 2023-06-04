Feature: Patient Payment Portal
  As a patient
  I want to be able to access my invoices
  So that I can pay my bills in time

  Scenario Outline: Paying bills
    Given An invoice "<invoice_number>" exists
    When I click on its "Pay" option
    And I enter the <amount> of money I want to pay
    And paid the amount in a certain "<time>"
    Then A payment record should be created documenting my payment

    Examples:
      | invoice_number | amount | time                |
      | INV-0001       | 50     | 2023-06-01 10:00 AM |
      | INV-0002       | 05     | 2023-06-01 10:00 AM |

Feature: Doctor Management
  As an administrator
  I want to be able to manage doctors
  So that I can create, read, update, and delete their entries

  Background:
    Given I am logged in as an administrator
    And I am in the "Doctors" section

  Scenario Outline: Register a doctor
    When I click on the "Add Doctor" button
    And I fill in <doctor_name>, <gmc_number>, <field> information
    And I click on the "Submit Doctor" button
    Then the entry should be added to the "Doctor" collection

    Examples:
      | doctor_name        | gmc_number | field       |
      | Richard Goodrich   | 7777777    | Orthopedist |
      | Christopher Turner | 8888888    | Neurologist |

  Scenario: Show a list of doctors
    When I look at the existing doctors
    Then I should be able to see a table of existing doctors

  Scenario Outline: Update a doctor entry
    Given a doctor with GMC number <gmc_number> exists
    When I edit <doctor_name>, <field> information of that doctor
    And I click on the "Update Doctors" button
    Then the entry should be updated in the "Doctor" collection

    Examples:
      | doctor_name         | gmc_number | field       |
      | Richard Badrich     | 7777777    | Orthopedist |
      | Christopher Spinner | 8888888    | Neurologist |

  Scenario Outline: Delete a doctor entry
    Given a doctor with GMC number <gmc_number> exists
    When I click on the "Delete" button of that doctor entry
    Then the entry should be deleted from the "Doctor" collection

    Examples:
      | gmc_number |
      | 7777777    |
      | 8888888    |

Feature: Doctor Management
  As an administrator
  I want to be able to manage doctors
  So that I can create, read, update, and delete their entries

  Scenario Outline: Register a doctor
    Given I am logged in as an administrator
    And I am in the "Doctors" section
    When I click on the "Add" button
    And I fill in <first_name>, <last_name>, <field> information
    And I click on the "Submit" button
    Then the entry should be added to the "Doctor" collection

    Examples:
      | first_name  | last_name | field       |
      | Richard     | Goodrich  | Orthopedist |
      | Christopher | Turner    | Neurologist |

  Scenario: Show a list of doctors
    Given I am logged in as an administrator
    When I click on the "Doctors" button in order to navigate to the related section
    Then doctors information should be returned

  Scenario Outline: Update a doctor entry
    Given I am logged in as an administrator
    And I am in the "Doctors" section
    When I select a doctor "<doctor_name>" from the list of doctors entries
    And I click on the "Update" button
    And I edit <first_name>, <last_name>, <field> information
    And I click on the "Submit" button
    Then the entry should be updated in the "Doctor" collection

    Examples:
      | doctor_name        | first_name  | last_name | field       |
      | Richard Goodrich   | Richard     | Goodrich  | Orthopedist |
      | Christopher Turner | Christopher | Turner    | Neurologist |

  Scenario Outline: Delete a doctor entry
    Given I am logged in as an administrator
    And I am in the "Doctors" section
    When I select a doctor "<doctor_name>" from the list of doctors entries
    And I click on the "Delete" button
    Then the entry should be deleted from the "Doctor" collection

    Examples:
      | doctor_name         |
      | Richard Goodrich    |
      | Christopher Turner  |

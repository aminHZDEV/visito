Feature: Admin Management
  As an administrator
  I want to be able to manage other administrators
  So that I can create, read, update, and delete their entries

  Scenario Outline: Register an administrator
    Given I am logged in as an administrator
    And I am in the "Admins" section
    When I click on the "Add" button
    And I fill in <first_name>, <last_name>, <username>, <password> information
    And I click on the "Submit" button
    Then the entry should be added to the "Admin" collection

    Examples:
      | first_name  | last_name | username  | password  |
      | Paul        | Goodrich  | abcdef    | 123       |
      | Don         | Turner    | ghijkl    | 123       |

  Scenario: Show a list of administrators
    Given I am logged in as an administrator
    When I click on the "Admins" button in order to navigate to the related section
    Then administrators information should be returned

  Scenario Outline: Update a administrator entry
    Given I am logged in as an administrator
    And I am in the "Admins" section
    When I select a administrator "<administrator_name>" from the list of administrators entries
    And I click on the "Update" button
    And I edit <first_name>, <last_name>, <username>, <password> information
    And I click on the "Submit" button
    Then the entry should be updated in the "Admin" collection

    Examples:
      | administrator_name  | first_name  | last_name | username  | password  |
      | Paul Goodrich       | Paul        | Goodrich  | abcdef    | 123       |
      | Don Turner          | Don         | Turner    | ghijkl    | 123       |

  Scenario Outline: Delete a administrator entry
    Given I am logged in as an administrator
    And I am in the "Admins" section
    When I select a administrator "<administrator_name>" from the list of administrators entries
    And I click on the "Delete" button
    Then the entry should be deleted from the "Admin" collection

    Examples:
      | administrator_name  |
      | Paul Goodrich       |
      | Don Turner          |

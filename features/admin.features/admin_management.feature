Feature: Admin Management
  As an administrator
  I want to be able to manage other administrators
  So that I can create, read, update, and delete their entries

  Background:
    Given I am logged in as an administrator
    And I am in the "Admins" section

  Scenario Outline: Register an administrator
    When I click on the "Add Admin" button
    And I fill in <administrator_name>, <username>, <password> information
    And I click on the "Submit Admin" button
    Then the entry should be added to the "Admin" collection

    Examples:
      | administrator_name | username | password |
      | John Goodrich      | abcdef   | 123      |
      | Richard Turner     | ghijkl   | 123      |

  Scenario: Show a list of administrators
    When I look at the existing admins
    Then I should be able to see a table of existing administrators

  Scenario Outline: Update a administrator entry
    Given an admin with username <username> exists
    When I edit <administrator_name>, <password> information of that administrator entry
    And I click on the "Update Admins" button
    Then the entry should be updated in the "Admin" collection

    Examples:
      | administrator_name | username | password |
      | Paul Goodrich      | abcdef   | 123      |
      | Don Turner         | ghijkl   | 123      |

  Scenario Outline: Delete a administrator entry
    Given an admin with username <username> exists
    When I click on the "Delete" button of that administrator entry
    Then the entry should be deleted from the "Admin" collection

    Examples:
      | username |
      | abcdef   |
      | ghijkl   |

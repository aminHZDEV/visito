Feature: Medicine Inventory Management
  As an administrator
  I want to be able to manage medicine inventory
  So that I can keep track of supplies and equipment

  Background:
    Given I am logged in as an administrator
    And I am in the "Inventory" section

  Scenario Outline: Add an item to the medicine inventory
    When I enter the item "<item_name>" that I want to add to inventory
    And I enter the quantity "<quantity>" of the item that I want to add to inventory
    And I click on the "Add Item" button
    Then the item should be added to the inventory

    Examples:
      | item_name | quantity |
      | Bandages  | 100      |
      | Syringes  | 50       |

  Scenario: Show a list of medicines
    When I look at the existing medications
    Then I should be able to see a table of existing medications

  Scenario Outline: Remove an item from the medicine inventory
    Given An entry for "<item_name>" exists
    When I click on the "Remove Item" button
    Then the item should be removed from the inventory

    Examples:
      | item_name |
      | Bandages  |
      | Syringes  |

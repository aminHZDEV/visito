Feature: Medicine Inventory Management
  As an administrator
  I want to be able to manage medicine inventory
  So that I can keep track of supplies and equipment

  Scenario Outline: Add an item to the medicine inventory
    Given I am logged in as an administrator
    And I am in the "Medicine Inventory" section
    When I enter the item "<item_name>" that I want to add to inventory
    And I enter the quantity "<quantity>" of the item that I want to add to inventory
    And I click on the "Add" button
    Then the item should be added to the inventory

    Examples:
      | item_name | quantity |
      | Bandages  | 100      |
      | Syringes  | 50       |

  Scenario: Show a list of medicines
    Given I am logged in as an administrator
    When I click on the "Medicine Inventory" button in order to navigate to its section
    Then medicines entries information should be returned

  Scenario Outline: Remove an item from the medicine inventory
    Given I am logged in as an administrator
    And I am in the "Medicine Inventory" section
    When I select the item "<item_name>" that I want to remove from inventory
    And I enter the quantity "<quantity>" of the item that I want to remove from inventory
    And I click on the "Remove" button
    Then the item should be removed from the inventory

    Examples:
      | item_name | quantity |
      | Bandages  | 10       |
      | Syringes  | 5        |

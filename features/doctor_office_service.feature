# Created by hamed at 5/29/23
Feature: doctor office service

  Scenario Outline: Doctor creates a new service
    When I add a service <name>, <price> and <duration>
    Then my service list should include <name>, <price> and <duration>

    Examples:
      | name         | price   | duration |
      | Consultation | $100.00 | 1        |
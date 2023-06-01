# Created by hamed at 5/30/23
Feature: Doctor and patient appointment
  Scenario Outline: Doctor schedules an appointment with a patient
    And I create an appointment in <date> and <time> for patient with name <name>
    Then an appointment in <date> and <time> for patient with name <name> is saved in database

    Examples:
      | name  | date       | time  |
      | Frank | 2023-06-01 | 10:00 |
      | Grace | 2023-06-02 | 11:30 |
      | Harry | 2023-06-03 | 14:00 |
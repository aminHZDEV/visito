# Created by hamed at 5/30/23
Feature: Doctor and patient appointment
  Scenario Outline: Doctor schedules an appointment with a patient
    When I create an appointment in <date> and <time> for patient with name <name>
    Then an appointment in <date> and <time> for patient with name <name> is saved in database

    Examples:
      | name  | date       | time  |
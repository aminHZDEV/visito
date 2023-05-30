Feature: Doctor office availability

  Scenario Outline: Doctor sets their availability for a day
    When I select a <date> from the calendar
    And I enter <start_time> and <end_time>
    Then I should receive a success message
    And my availability calendar should show that date as available from <start_time> to <end_time>

    Examples:
      | date       |  | start_time |  | end_time |  |
      | 2023-06-05 |  | 09:00      |  | 12:00    |  |
      | 2023-06-06 |  | 13:00      |  | 17:00    |  |
      | 2023-06-07 |  | 10:00      |  | 15:00    |  |
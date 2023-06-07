Feature: Doctor office availability

  Scenario Outline: Doctor sets their availability for a day
    When I select a <date> from the calendar
    And I enter <start_time> and <end_time>
    Then I should receive a success message
    And my availability calendar should show that date as available from <start_time> to <end_time>

    Examples:
      | date       |  | start_time |  | end_time |  |

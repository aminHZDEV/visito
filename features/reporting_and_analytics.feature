Feature: Reporting and Analytics
  As an administrator
  I want to be able to generate reports and analytics
  So that I can get insights into the operations and performance

  Scenario Outline: Generate a report for a specific time period
    Given I am logged in as an administrator
    And I am in the "Reports and Analytics" section
    When I select the time period "<time_period>" for which I want to generate a report
    And I select the type of report "<report_type>" that I want to generate
    And I click on the "Generate Report" button
    Then a report for the selected time period with the selected report type should be generated

    Examples:
      | time_period              | report_type    |
      | 2023-01-01 to 2023-06-01 | Patient Visits |
      | 2023-01-01 to 2023-06-01 | Revenue        |

  Scenario Outline: Generate analytics for a specific time period
    Given I am logged in as an administrator
    And I am in the "Reports and Analytics" section
    When I select the time period "<time_period>" for which I want to generate analytics
    And I select the type of analytics "<analytics_type>" that I want to generate
    And I click on the "Generate Analytics" button
    Then an analytics for the selected time period with the selected analytics type should be generated

    Examples:
      | time_period              | analytics_type |
      | 2023-01-01 to 2023-06-01 | Patient Visits |
      | 2023-01-01 to 2023-06-01 | Revenue        |

Feature: Reporting and Analytics
  As an administrator
  I want to be able to generate reports
  So that I can get insights into the operations and performance

  Scenario Outline: Generate a report for a specific time period
    Given necessary collections exist
    And I am logged in as an administrator
    And I am in the "Reports" section
    When I select the time period "<time_period>" for which I want to generate a report
    And I select the type of report "<report_type>" that I want to generate
    And I click on the "Generate" button
    Then a report for the selected time period with the selected report type should be generated

    Examples:
      | time_period              | report_type    |
      | 2023-01-01 to 2023-06-05 | Patient Visits |
      | 2023-01-01 to 2023-06-05 | Revenue        |
    
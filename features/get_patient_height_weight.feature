# Created by Taravat Monsef
Feature: get patient height weight
  As a doctor I want to add to patient records
  so I log into the patient record system
  and add his/her height and weight

  Scenario Outline: Add Height and Weight to Patient Record
    Given the doctor is logged into the patient <patient_id> record system
    When they enter new <height>  and <weight> for the patient
    Then the system should update the patient record

    Examples:
      | patient_id  | height        | weight       |
      | 1           | 167           | 50           |
      | 2           | 177           | 56           |
      | 3           | 166           | 66           |
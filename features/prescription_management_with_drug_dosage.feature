# Created by Narges Abbasi
Feature: Prescription Management with Drug Dosage

  Scenario Outline: Write a prescription for a patient
    Given I'm doctor
    And I want to write a prescription for a patient
    When I enter the patients information
    And I prescribe <drug> with <dosage>
    Then the prescription should be written successfully

    Examples:
      | drug          | dosage      |
      | Amoxicillin   | 500mg       |
      | Ibuprofen     | 200mg       |
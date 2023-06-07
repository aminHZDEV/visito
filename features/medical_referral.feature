Feature: Medical Referral

  Scenario Outline: Doctor refers patient to specialist
    Given the doctor recommends a referral to <specialist>
    When the system generates a <referral_request>
    Then the system should send the referral request to the <specialist_office>
    And the system should notify the patient of the referral request

    Examples:
    | specialist            | referral_request                                                                                                      | specialist_office                                                        |
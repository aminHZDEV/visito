Feature: Prescription Refill Request

  Scenario Outline: Patient requests medication refill
    Given the patient wants to request a prescription refill
    When the patient requests a refill for <medication_name>
    Then the system should confirm the <prescription_details>
    And the system should send a prescription refill request to the doctor for approval

    Examples:
    | medication_name       | prescription_details                                    |
    | "Amoxicillin"         | "dosage and frequency of Amoxicillin"                   |
    | "Zoloft"              | "current prescription details for Zoloft"               |
    | "Lantus"              | "last filled date and quantity of Lantus"               |
    | "Simvastatin"         | "dosage and frequency of Simvastatin"                   |
    | "Ventolin"            | "current prescription details for Ventolin"             |
    | "Metoprolol"          | "last filled date and quantity of Metoprolol"           |
    | "Synthroid"           | "dosage and frequency of Synthroid"                     |
    | "Nexium"              | "current prescription details for Nexium"               |
    | "Tramadol"            | "last filled date and quantity of Tramadol"             |
    | "Cymbalta"            | "dosage and frequency of Cymbalta"                      |
    | "Hydrochlorothiazide" | "current prescription details for Hydrochlorothiazide"  |
    | "Omeprazole"          | "last filled date and quantity of Omeprazole"           |

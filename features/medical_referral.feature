Feature: Medical Referral

  Scenario Outline: Doctor refers patient to specialist
    Given the doctor recommends a referral to <specialist>
    When the system generates a <referral_request>
    Then the system should send the referral request to the <specialist_office>
    And the system should notify the patient of the referral request

    Examples:
    | specialist            | referral_request                                                                                                      | specialist_office                                                        |
    | Dr. Jane Lee          | Referral from Dr. John Smith to Dr. Jane Lee (Oncology) for Mrs. Barbara Davis with breast cancer                     | Cedar Sinai Oncology Center (Los Angeles, CA)                            |
    | Dr. Carlos Rodriguez  | Referral from Dr. Emily Chen to Dr. Carlos Rodriguez (Neurology) for Mr. Jose Hernandez with Parkinson's Disease      | University of Miami Neurology Clinic (Miami, FL)                         |
    | Dr. Jennifer Patel    | Referral from Dr. Michael Chang to Dr. Jennifer Patel (Dermatology) for Ms. Maria Gomez with eczema                   | Johns Hopkins Dermatology Clinic (Baltimore, MD)                         |
    | Dr. Steven Jacobs     | Referral from Dr. Alex Nguyen to Dr. Steven Jacobs (Cardiology) for Mr. David Kim with heart palpitations             | Mayo Clinic Cardiology Center (Rochester, MN)                            |
    | Dr. Rachel Singh      | Referral from Dr. Lisa Patel to Dr. Rachel Singh (Gastroenterology) for Mr. Robert Jones with ulcerative colitis      | Cleveland Clinic Gastroenterology Center (Cleveland, OH)                 |
    | Dr. Abdul Aziz Al-Ali | Referral from Dr. Fatima Ahmed to Dr. Abdul Aziz Al-Ali (Endocrinology) for Mrs. Aisha Mohammed with type 2 diabetes  | King Faisal Specialist Hospital & Research Centre (Riyadh, Saudi Arabia) |
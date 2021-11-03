Feature: Registration Feature
  Scenario Outline: Validating the Registration Feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    And I enter the phone number as "<Phone number>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    Then I click on the submit button
    Examples:
      | name        | Phone number | email           | country | city   | username | password |
      | A Mukherjee | 8900560944   | test@email.com  | India   | Kolkata| amkh     | asdfsdfdf|
      | S Mukherjee | 9711911558   | smkh@email.com  | Germany | Berlin | smkh     | werwerwer|
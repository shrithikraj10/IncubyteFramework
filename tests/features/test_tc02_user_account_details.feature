Feature: Parabank user account details
  To verify user can view/access account details

  Scenario: Verify user is able to login and view account balance
    Given I navigate to the Parabank home page
    When I am able to successfully login to my account
    Then I am able to view my account balance
 


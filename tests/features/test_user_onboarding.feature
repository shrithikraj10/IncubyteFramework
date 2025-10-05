Feature: Parabank new user onboaring and authentication
  To verify that a new user can sign up and log in successfully

  Scenario: Verify user is able to signup and create a Parabank account
    Given I navigate to the Parabank home page
    Then I am able to successfully register a new user account
 
  Scenario: Verify user is able to login with the new account created
   Given I navigate to the Parabank home page
   Then I am able to successfully login to the new user account


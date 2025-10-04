Feature: Parabank Signup and Login
  To verify that a user can sign up and log in successfully

  Scenario: Successful signup and login
    Given I navigate to the Parabank registration page
    When I create a new user account
    And I log in with that account
    Then I should see my account balance displayed

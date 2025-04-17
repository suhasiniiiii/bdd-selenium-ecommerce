Feature: Login functionality on SauceDemo eCommerce site

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enter valid username and password
    And the user clicks on login button
    Then the user should be logged in successfully

  Scenario: Login with invalid credentials
  Given the user is on the login page
  When the user logs in with invalid credentials
  And the user clicks on login button
  Then the login should fail with an error message


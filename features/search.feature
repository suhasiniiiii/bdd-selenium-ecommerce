Feature: Search functionality on SauceDemo eCommerce site

  Scenario Outline: Search for a product
    Given user is on homepage
    When user searches for "<product>"
    Then products related to "<product>" should be displayed

    Examples:
      | product |
      | Backpack |
      | Bike    |

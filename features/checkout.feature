Feature: Checkout process
Scenario Outline: Complete checkout process
  Given user is on homepage
  When user selects "<product>"
  And adds product to the cart
  And selects the cart
  Then the product should be displayed there
  When user selects checkout
  And enters first name
  And enters last name
  And enters postal code
  And clicks on continue
  Then the checkout overview should be displayed
  When user clicks on finish
  Then the order should be placed successfully

   Examples:
      | product |
      |Sauce Labs Backpack|


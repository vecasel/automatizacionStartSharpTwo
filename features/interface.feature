Feature: Login and interface verification

  As a Serenity user
  I want to log in and verify that interface elements are displayed correctly
  So that I can ensure everything is working properly

  Scenario: Log in and verify interface elements
    Given I am on the login page
    When I enter my user credentials "admin" and password "serenity"
    And I click the "Log in" button
    Then I should see the title "Dashboard - StartSharp"
    And there should be at least one icon visible on the page
    And there should be at least one button visible on the page
    And there should be at least one text field visible on the page
    And there should be at least one image visible on the page
    And I should see the title "Dashboard" on the page



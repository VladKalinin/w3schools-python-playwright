Feature: Home Page Functionality

  Scenario Outline: Verify top navigation header contains all sections
    Given Browser is on Home Page
    Then following <section> are displayed on Top Header On Home Page

    Examples:
      | section                                   |
      | Tutorials,Exercises,Certificates,Services |
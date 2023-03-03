Feature: Online Learning Site's Search Option

    Background:Launch Browser and app
    Given Chrome is opened and Unacademy app is opened

    Scenario Outline: Validate that the User is able to type the name of the course onto the Search Bar.
    When User navigates onto the Search Option of the Site
    And User clicks onto the Search Option of the Site
    And User send <coursename>
    Then It shows the Courses
    Examples:
    | coursename |
    | JEE        |

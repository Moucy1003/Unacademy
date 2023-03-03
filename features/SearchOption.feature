Feature: Online Learning Site's Search Option

  Scenario: Validate that the user is able to navigate on to the Website's page.
    Given Chrome is opened and Unacademy app is opened
    Then  User navigates onto the site and the Search Option is visible

   Scenario: Validate that the User is able to see the list of the popular searches when the User clicks on the Search Option.
   Given Chrome is opened and Unacademy app is opened
   When User navigates onto the Search Option of the Site
   And User clicks onto the Search Option of the Site
   Then It shows the list of popular searches available in the Site

   Scenario Outline: Validate that the User is able to type the name of the course onto the Search Bar.
   Given Chrome is opened and Unacademy app is opened
   When User navigates onto the Search Option of the Site
   And User clicks onto the Search Option of the Site
   And User types the name "<coursename>" of the desired Course
   Then It shows the Courses as a dropdown list to choose from
   Examples:
   | coursename |
   | JEE        |
   | GATE       |

    Scenario Outline: Validate Search Option's Functionality with valid data
      Given Chrome is opened and Unacademy app is opened
      When User clicks onto the Search Option and enters"<validcoursename>"
      And User clicks onto the desired Course name
      Then It shows the desired course webpage
      And Chrome is closed
      Examples:
      | validcoursename         |
      |  Full Stack Development |



    Scenario Outline: Validate Search Option's Functionality with invalid data
    Given Chrome is opened and Unacademy app is opened
    When User enters <invalidcoursename>
    Then It gives the No goals found message
    And Chrome is closed
    Examples:
    | invalidcoursename |
    | asdfg             |
    | chocolate         |













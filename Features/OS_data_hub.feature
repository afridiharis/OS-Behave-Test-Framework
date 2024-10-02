@regression @smoke
Feature: OS Data Hub verification

  @homepage
  Scenario: Verify OS Data Homepage
    Given I am on the OS Data homepage
    Then page title should include "OS Data Hub"
    And verify header menu is as expected as below
        | header_menu_options |
        | API Dashboard, Download, Docs, Support, Plans |
    And header text should say "Welcome to the OS Data Hub"
    And check "Sign up for free" and "Explore and access OpenData" buttons are displayed
    And check animation containers are displayed

  @api_page
  Scenario: Verify API Dashboard page
    Given I am on the OS Data homepage
    When I click on "API Dashboard" header menu button
    Then page title should include "API Dashboard"
    And header text should say "Dashboard"
    And on the sidebar it should say "Dashboard"
    And text links should say "log in", "sign up" and "documentation" on main content of the page

  @download_page
  Scenario: Verify Download page
    Given I am on the OS Data homepage
    When I click on "Download" header menu button
    Then page title should include "Download"
    And on the sidebar it should say "OpenData downloads"
    And header text should say "OpenData Downloads"
    And I can see the search bar
    And I can see the filters below the search bar as below
        | filter_type       |
        | All types of data |
        | All data providers|
    And I can see all the download results displayed on the page

  @docs_page
  Scenario: Verify Docs page
    Given I am on the OS Data homepage
    When I click on "Docs" header menu button
    Then page title should include "API Documentation"
    And header text should say "Documentation"
    And on the sidebar it should say "Docs"
    And verify all the links on the sidebar when expanding using details below
       | side_menu_links |
       | Overview, Getting started guide, Technical specification |

  @support_page
  Scenario: Verify Support page
    Given I am on the OS Data homepage
    When I click on "Support" header menu button
    Then page title should include "OS OpenData FAQ's"
    And side bar menu should show expanded faq links as below
        | faqs_sub_links |
        | Account and API, Plans, Download, OS Select+Build |
    And check all faqs are there

  @plans_page
  Scenario: Verify Plans page
    Given I am on the OS Data homepage
    When I click on "Plans" header menu button
    Then page title should include "Plans"
    And sub heading should say "Choose Your Plan"
    And all three plans should be shown as below
        | plans |
        | OS OpenData Plan, Premium Plan, Public Sector Plan |


*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          LoginPage.open the web page for the validation        #Keyword written in the resource file
Test Teardown       LoginPage.Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Resource            ../Selenium-RFW/PageObjects/HomePage.robot
Resource            ../Selenium-RFW/PageObjects/LoginPage.robot


*** Variables ***

*** Test Cases ***
Validate the user unsuccessful login
    fill the login form     ${user_name}    ${invalid_password}
    wait until it finds     ${errorMsgLocator}
    verify the error message is correct

Validate the user successful login
    fill the login form     ${user_name}    ${valid_password}
    wait until it finds     ${successfullLogin}

*** Keywords ***


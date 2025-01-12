*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Test Template       Validate the user unsuccessful login
Library             DataDriver      file=resources.csv      encoding=utf8       dialect=unix            #it has to be added.

*** Variables ***
${errorMsgLocator}      css:.alert-danger

#keep this all in a excel file
#*** Test Cases ***      username                password
#Invalid username            sharath                 learning
#Invalis password            rahulshettyacademy      1234
#Special charecters          @%^                     *&^

*** Test Cases ***
Login with user ${username} and password ${Password}        sharath     1234
#Even though there is no test cases also we have to write atleast one otherwise the robotframework will get confused.
#if we forget to give the test case name and if we keep blank then this one will be picked a test case name
#when we given wrong file name "Library             DataDriver      file=fdghfjfufuf.csv" then also,it will execute with default things given above

*** Keywords ***
Validate the user unsuccessful login
    [Arguments]     ${username}     ${password}     #these arguments name should be same as the parameters name in excel  or change those parameters as mentioned here eith $
    fill the login form     ${user_name}    ${invalid_password}
    wait until it finds     ${errorMsgLocator}
    verify the error message is correct

fill the login form
    [arguments]     ${userName}     ${pwd}
    Input Text      id:username     ${userName}
    Input Password  id:password     ${pwd}
    Click Button    signInBtn

wait until it finds
    [arguments]     ${locator}
    Wait Until Element Is Visible   ${locator}

verify the error message is correct
    Element Text Should Be      ${errorMsgLocator}  Incorrect username/password.

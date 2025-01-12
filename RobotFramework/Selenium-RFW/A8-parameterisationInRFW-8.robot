*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Test Template       Validate the user unsuccessful login

*** Variables ***
${errorMsgLocator}      css:.alert-danger
${successfullLogin}     css:a.nav-link

*** Test Cases ***      username                password
Invalid username            sharath                 learning
Invalis password            rahulshettyacademy      1234
Special charecters          @%^                     *&^


*** Keywords ***
Validate the user unsuccessful login
    [Arguments]     ${username}     ${password}
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
    #commented below two lines of code and used something other instead of that's also same.
    #${text_resp} =  Get Text    ${errorMsgLocator}#declared the locator at the variable section.
    #Should Be Equal As Strings  ${text_resp}    Incorrect username/password.
    Element Text Should Be      ${errorMsgLocator}  Incorrect username/password.

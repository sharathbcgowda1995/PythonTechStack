*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file

*** Variables ***
${errorMsgLocator}  css:.alert-danger

*** Test Cases ***
Validate the user unsuccessful login
    fill the login form with wrong credentilas
    wait until it checks & displays the error message
    verify the error message is correct

*** Keywords ***

fill the login form with wrong credentilas
    Input Text      id:username     ${userName}
    Input Password  id:password     ${invalid_password}
    Click Button    signInBtn

wait until it checks & displays the error message
    Wait Until Element Is Visible   ${errorMsgLocator}

verify the error message is correct
    #commented below two lines of code and used something other instead of that's also same.
    #${text_resp} =  Get Text    ${errorMsgLocator}#declared the locator at the variable section.
    #Should Be Equal As Strings  ${text_resp}    Incorrect username/password.
    Element Text Should Be      ${errorMsgLocator}  Incorrect username/password.

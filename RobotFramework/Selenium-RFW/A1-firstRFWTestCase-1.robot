*** Settings ***
Documentation   Validate the login form
Library         SeleniumLibrary
Test Teardown       Close Browser        #here we can write sentence and we can give the body.

*** Variables ***
${base_url}     https://www.rahulshettyacademy.com/loginpagePractise/
${errorMsgLocator}  css:.alert-danger

*** Test Cases ***
Validate the user unsuccessful login
    open the web page for the validation
    fill the login form with wrong credentilas
    wait until it checks & displays the error message
    verify the error message is correct

*** Keywords ***
open the web page for the validation
    create webdriver    Chrome
    Go To       ${base_url}

fill the login form with wrong credentilas
    Input Text      id:username     rahulshettyacademy
    Input Password  id:password     12345678
    Click Button    signInBtn

wait until it checks & displays the error message
    Wait Until Element Is Visible   ${errorMsgLocator}

verify the error message is correct
    #commented below two lines of code and used something other instead of that's also same.
    #${text_resp} =  Get Text    ${errorMsgLocator}#declared the locator at the variable section.
    #Should Be Equal As Strings  ${text_resp}    Incorrect username/password.
    Element Text Should Be      ${errorMsgLocator}  Incorrect username/password.

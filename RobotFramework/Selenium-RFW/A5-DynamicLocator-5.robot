*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Library             Collections

*** Variables ***

${successfullLogin}     css:a.nav-link

*** Test Cases ***

Validate the user has selected the specific mobile phone
    fill the login form     ${user_name}    ${valid_password}
    wait until it finds     ${successfullLogin}
    need to select the balckberry   Blackberry

*** Keywords ***

fill the login form
    [arguments]     ${userName}     ${pwd}
    Input Text      id:username     ${userName}
    Input Password  id:password     ${pwd}
    Click Button    signInBtn

wait until it finds
    [arguments]     ${locator}
    Wait Until Element Is Visible   ${locator}

need to select the balckberry
    [arguments]     ${phoneSelected}
    @{listOfWebElements}=       Get WebElements      css:h4.card-title
    ${index}=   Set Variable    1
    FOR	${var}	IN	@{listOfWebElements}
        log to console     ${var.text}
        Exit For Loop If    '${phoneSelected}==${var.text}'
        ${index}=   Evaluate    ${index}+1
    END
    click button    xpath:(//*[@class='card-footer'])[${index}]/button
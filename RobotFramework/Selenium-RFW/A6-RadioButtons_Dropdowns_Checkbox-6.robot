*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Library             Collections

*** Variables ***

*** Test Cases ***

Validate the user has handled the radio buttons and dropdowns
    fill the login form     ${user_name}    ${valid_password}
    select the dropdown_checkbox and handle the dropdown


*** Keywords ***

fill the login form
    [arguments]     ${userName}     ${pwd}
    Input Text      id:username     ${userName}
    Input Password  id:password     ${pwd}

select the dropdown_checkbox and handle the dropdown
    click element   xpath:(//span[@class='checkmark'])[2]
    Wait Until Element Is Visible   css:.modal-body
    Click button   xpath://button[@id='okayBtn']     #Written multiple times as it was not selecting for only one time.
    Click button   xpath://button[@id='okayBtn']
    Click button   xpath://button[@id='okayBtn']
    Click button   xpath://button[@id='okayBtn']     #Written multiple times as it was not selecting for only one time.
    Click button   xpath://button[@id='okayBtn']
    Click button   xpath://button[@id='okayBtn']
    Wait Until Element Is Not Visible   css:.modal-body
    Select From List By Value   css:select.form-control     teach
    Select Checkbox     terms
    Checkbox Should Be Selected     terms
    Click Button    signInBtn
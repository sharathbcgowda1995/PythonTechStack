*** Settings ***
Documentation   Validate the login form
Library         SeleniumLibrary
Test Setup      open the web page for the validation
Test Teardown       Close Browser           #here we can write sentence and we can give the body.
Resource        A-resource.robot
Library             Collections
Library             String

*** Variables ***
${base_url}     https://www.rahulshettyacademy.com/loginpagePractise/

*** Test Cases ***
Handling the child windows and extracting the text using string functions.
    click on the link to open the child window
    Switch to the child window
    Validate whether you have been switched to child window or not
    Switch back to the parent window and print the emailid from the child window

*** Keywords ***
click on the link to open the child window
    click element   css:.blinkingText
    Sleep           5

Switch to the child window
    Sleep           5
    switch window   NEW

Validate whether you have been switched to child window or not
    ${title}=   Get Title
    Log To Console    ${title}
    Should Be Equal     ${title}    Rahul Shetty Academy
    Sleep       5
    ${text}=    get text    xpath://h3/span         #to grab the text from web element
    @{splittedString}=      Split String    ${text}         #To split the string
    ${variable}     Protractor                      #error is No keyword with name 'Protractor' found.
    Set Global Variable     ${variable}                 #
    #FOR	${var}	IN	${splittedString}               #to iterate over the list rfw
       # Log     ${var}
       # Continue For Loop If	'${var}[7]'!='Protractor,'
       # ${tech}=  ${var}
        #log     ${tech}
    #END

Switch back to the parent window and print the emailid from the child window
    switch window   MAIN
    Input Text      id:username     ${variable}
    Input Password  id:password     1234

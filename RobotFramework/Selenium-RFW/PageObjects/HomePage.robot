*** Settings ***
Documentation       If we have multiple reusable codes like test data,url,keywords amd
...                 open and closing the nrowser then we can store that in one of the robot file as resource.

Library             SeleniumLibrary

*** Variables ***
${successfullLogin}     css:a.nav-link

*** Keywords ***
wait until it finds
    [arguments]     ${locator}
    Wait Until Element Is Visible   ${locator}
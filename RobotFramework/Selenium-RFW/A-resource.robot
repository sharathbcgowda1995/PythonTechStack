*** Settings ***
Documentation       If we have multiple reusable codes like test data,url,keywords amd
...                 open and closing the nrowser then we can store that in one of the robot file as resource.

Library             SeleniumLibrary

*** Variables ***
${url}                  https://www.rahulshettyacademy.com/loginpagePractise/
${user_name}            rahulshettyacademy
${invalid_password}     1234
${valid_password}       learning

*** Keywords ***
open the web page for the validation
    create webdriver    Chrome          #path arg is not needed as it's mentioned in bin of mac
    Go To       ${url}

Close the current browser
    close browser
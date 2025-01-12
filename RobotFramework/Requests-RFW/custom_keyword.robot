*** Settings ***
Library     RequestsLibrary
Library     Collections
Library     ../Requests-RFW/CustomLibraries/customKeywords.py

*** Variables ***

${base_url} =
${endpoint} =   /Number/
${username} =
${password} =
${status_code} =    200

*** Test Cases ***
Retrieving all the user rented numbers.
    ${response}     Create session with the basic authentication        ${base_url}     ${username}     ${password}
    Set Global Variable    ${response}
    Log the status code of the GET api     ${response}
    Call the get API to fetch all the rented numbers
    validate the response with the expected status code         ${status_code}
    Log the response of the GET api     ${response}

*** Keywords ***
Log the response of the GET api
    [Arguments]     ${response}
    log to console      ${response.content}

Log the status code of the GET api
    [Arguments]     ${response}
    log to console      ${response.status_code}
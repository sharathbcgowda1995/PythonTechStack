*** Settings ***
Library  RequestsLibrary
Library     Collections

*** Variables ***

${base_url} =
${endpoint} =   /Number/
${username} =
${password} =
${response} =   response from the api call

*** Test Cases ***
Retrieving all the user rented numbers.
    Create session with the basic authentication
    Call the get api to retrieve all the rented numbers
    Get the status code and validate with the expected
    Log the response to the console

*** Keywords ***
Create session with the basic authentication
        ${auth} =   create list     ${username}    ${password}
        create session   mysession  ${base_url}    auth=${auth}

Call the get api to retrieve all the rented numbers
        ${response} =    get request    mysession  ${endpoint}
        Set Global Variable    ${response}

Get the status code and validate with the expected
        ${code} =   convert to string   ${response.status_code}
        should be equal  ${code}    200

Log the response to the console
        log to console   ${response.content}
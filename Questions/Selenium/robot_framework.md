Command analysis :
robot -P . -v env:local -v user:plivonumbers --i port_in_regression Functional/Porter/Port_In.robot

robot: 
This is the command to execute the Robot Framework. It is followed by various options and arguments.

-P .: 
This option sets the path to search for Python modules. In this case, . refers to the current directory.

-v env:local: 
This option sets a variable named env with the value local. This variable might be used within the Robot Framework test suite or test cases.

-v user:plivonumbers: 
This option sets another variable named user with the value plivonumbers. Similar to the previous option, 
this variable may be used within the test suite or test cases.

--i port_in_regression: 
This option specifies the tags to include during test execution. Tests or test cases in the specified test suite that have the tag port_in_regression will be included.

Functional/Porter/Port_In.robot: 
This is the path to the Robot Framework test suite file that you want to execute. In this case, it is Functional/Porter/Port_In.robot. 
The path is relative to the current directory.

[
*** Settings ***
Library           DateTime
Variables   ../../Resources/${env}.py
Library     ../../Functional/Library/ApiCall/Inventory.py         ${data}     ${user}
Library     ../../Functional/Library/ApiCall/Inventory_dbcfg.py   ${data}
Library     robot.libraries.String
Library     BuiltIn

Documentation
...         This test suite is to test port in internal apis

Suite Setup  Create porting request
Suite Teardown  Cleanup Inventory

*** Variables ***
#${user_auth}                                   MAYJLIZGQ5MWVKZWM4NZ
${user_auth}                                    MAOWI4NWU1YJU3ZJK4ZM
${existing_phone_number}                        19018053009

*** Test Cases ***
Regression TC to check E2E port-in flow for [Received FOC + Complete] statuses from IQ - Local flow
    [Tags]      port_in_regression      port_in_sanity
    ${E2E_Local_flow_TN}      validate_number_availability    ${available_number}
    Set Global Variable    ${E2E_Local_flow_TN}
    read_and_edit_s3_file   ${E2E_Local_flow_TN}    ${E2E_Local_flow_TN}    ${Received_FOC}     ${automation_flow}     ${port_in_flow}
    ${Local_E2E_regression}    create dictionary        email_id=${test_email}       alias=Automation_E2E_Test_${alias}      requested_port_date=${requested_port_date}      salutation=Mr      end_user_type=individual      first_name=Plivo   last_name=Inc     address_line_1=01   city=Bangalore  state=California     country_iso2=US     zip_code=10001     number_type=local     numbers=${E2E_Local_flow_TN}     files=${EXECDIR}/Functional/Resources/images/LocalPDF.pdf
    ${business_request_id}   Create port in order    &{Local_E2E_regression}
    log     ${business_request_id}
    call_wait   30
    ${port_status}      ${rejection_reason}     get_the_details_of_number     ${E2E_Local_flow_TN}
    verify_the_details_of_number    ${submitted_carrier}    ${port_status}

*** Keywords ***
Create porting request
    ${current_date}  Get Current Date    result_format=datetime
    ${requested_port_date}  Add Time To Date  ${current_date}  15 days
    ${requested_port_date}  Convert Date    ${requested_port_date}  result_format=%Y-%m-%d
    log  ${requested_port_date}

Add accepted number to inventory
    ${response}   return_numbers_from_inventory   test.numbers@plivo.com   ${phone_number_business}
    BuiltIn.Sleep   30
    Log    ${response}

Cleanup Inventory
    ${response}   return_numbers_from_inventory   ${test_email}      ${phone_number_individual}
    ${response}   return_numbers_from_inventory   ${test_email}      ${phone_number_business}
]
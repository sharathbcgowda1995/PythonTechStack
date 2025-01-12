*** Settings ***
Documentation       Validate the login form                     #Description of the test case or feature
Library             SeleniumLibrary                             #Library needed for UI Automation
Test Setup          open the web page for the validation        #Keyword written in the resource file
Test Teardown       Close the current browser                   #here we can write sentence and we can give the body.
Resource            A-resource.robot                              #It links the all needed things for this file
Library             Collections
Library             ../CustomLibraries/Shop.py
Library             Shop.py

*** Variables ***
${errorMsgLocator}      css:.alert-danger
${successfullLogin}     css:a.nav-link
${selectMobiles}        Nokia Edge      Blackberry

*** Test Cases ***
Validate the user successful login
    fill the login form     ${user_name}    ${valid_password}
    wait until it finds     ${successfullLogin}
    add to cart and checkout    ${selectMobiles}    #substitution for the #validate the login page with mobile devices

*** Keywords ***

fill the login form
    [arguments]     ${userName}     ${pwd}
    Input Text      id:username     ${userName}
    Input Password  id:password     ${pwd}
    Click Button    signInBtn

wait until it finds
    [arguments]     ${locator}
    Wait Until Element Is Visible   ${locator}

#validate the login page with mobile devices
    #@{listOfWebElements}=       Get WebElements      css:h4.card-title #to get common webelements
   # @{actualList} =     Create List                                    #creates the empty list
    #FOR	${var}	IN	@{listOfWebElements}                               #forloop
      #  Log     ${var.text}
     #   Append To List  ${actualList}   ${var.text}                    #adding the data to the list
    #END
    #${expectedList}=    create list   iphone X      Samsung Note 8      Nokia Edge      Blackberry      #Creating a list

    #lists should be equal  ${expectedList}  @{actualList}               #comparing two lists
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing UN and the passwod along with the URL as below to handle the authentication pop ups
#Syntax - https://UN:PWD@the-internet.herokuapp.com/basic_auth
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#validation
val = driver.find_element(By.XPATH,value="//div//p").text
if val == "Congratulations! You must have the proper credentials." :
    print("Authentication pop up is handled successfully....")
else:
    print("Failed to handle the authentication pop ups....")

time.sleep(5)
driver.quit()
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url to open the web applications on the same tab.
driver.get("https://admin-demo.nopcommerce.com/login")

#text - to get the iner text.
textVal =driver.find_element(By.XPATH,value="//button[normalize-space()='Log in']").text
print("Actual usage of text : ",textVal)

#get_attribute - to get the value of any attribute of the web element.
element = driver.find_element(By.ID,value="Email")
print("Actual use of the get_attribute : ",element.get_attribute("id"))

print("before passing value to the VALUE attribute it prints the default value present there : ",element.get_attribute("value"))
element = driver.find_element(By.ID,value="Email")
element.clear(),element.send_keys("sharathbc")
print("after passed value to the VALUE attribute : ",element.get_attribute("value"))
print("Trying to use the text on the WE which has no innert text and the response should be null : ", element.text)
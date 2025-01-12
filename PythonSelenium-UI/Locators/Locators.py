#Locators
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com")

#ID
#Most of the time to get the all the links
driver.find_element(By.ID,value="email").send_keys("sharath@123.com")

#CALSS_NAME
#To write generis locator to grab the WE accordingly.
driver.find_element(By.CLASS_NAME,value="inputtext").send_keys("hello@123")

#NAME
driver.find_element(By.NAME,value="login").click()

#PARTIAL_LINK_TEXT
#we use this wherever there is a anchor or link.
driver.find_element(By.PARTIAL_LINK_TEXT,value="Forgotten pas").click()

#syncup
time.sleep(3)

#LINK_TEXT
#we use this wherever there is a anchor or link.
driver.find_element(By.LINK_TEXT,value="Forgotten account?").click()

time.sleep(3)
driver.close()
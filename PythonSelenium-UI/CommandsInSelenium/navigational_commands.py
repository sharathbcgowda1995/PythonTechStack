import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url to open the web applications on the same tab.
driver.get("https://www.amazon.com/")
driver.get("https://www.flipkart.com/")

#to go back we have method called .back() which can be used with the driver instances.
driver.back()

#to go forward we have a method called .forward()
driver.forward()

#to refresh the existing page we have
driver.refresh()

#difference between find_element and find_elements
driver.find_element(By.LINK_TEXT,value="Today's Deals")

time.sleep(3)
driver.quit()

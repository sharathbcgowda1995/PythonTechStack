import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://opensource-demo.orangehrmlive.com/")

#open other tab and observe the changes.
driver.find_element(By.LINK_TEXT,value="OrangeHRM, Inc").click()

time.sleep(3)

#it is driver focuse hence it will close the web tab which is opened first or which is mentioned as URL
#driver.close()

#quit()- will close all the associated web tabs and it's process focused so it kills all the processes and that leads to
#killing of all the associated tabs.
driver.quit()
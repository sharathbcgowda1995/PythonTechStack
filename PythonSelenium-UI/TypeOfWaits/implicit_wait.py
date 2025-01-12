import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url to open the web applications on the same tab.
driver.get("https://www.google.com/")

#1.implicitly_wait(sec) -- which applies to all the WE in this script
driver.implicitly_wait(5)

#Google as selenium and voice prompt will pop up with some delay sync up with implicitly_wait(sec) to click on no thanks.
element = driver.find_element(By.XPATH,value="//input[@title='Search']")
element.send_keys("Selenium")

#this is actually taking time to visible on DOM hence here the implicit wait will work till it populate
driver.find_element(By.XPATH,value="//button[@aria-label='No thanks' or @class='M6CB1c rr4y5c']").click()

time.sleep(5)
driver.quit()



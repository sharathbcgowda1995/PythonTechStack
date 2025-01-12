import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url to open the web applications on the same tab.
driver.get("https://www.google.com/search?q=selenium&oq=selenium&aqs=chrome.0.69i59j0i131i433i512j69i59j0i433i512j69i60l4.1549j0j7&sourceid=chrome&ie=UTF-8")

#2.explicit_wait
#synatx 1 - my_wait= WebDriverWait(driver,10)
#Syntax 2 - my_wait= WebDriverWait(driver,10,poll_frequency=2)
#Syntax 3 - here simply use Exception if you don't want to explicitly mention all this exceptions.
my_wait= WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotVisibleException,Exception])


#using the explicit wait as below.
#This part should be completely inside the brackets (By.XPATH,("//h3[normalize-space()='Selenium']"))
web_element  = my_wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
web_element.click()

time.sleep(5)
driver.quit()
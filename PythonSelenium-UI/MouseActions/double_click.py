#Don't run

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/default.asp")

time.sleep(4)

#switch to frame.
driver.switch_to.frame("nameOfTheFrame")

#double clickable element
double_click_element = driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b")

#Initiate the double click operation
act = ActionChains(driver)

#after this operation it will show the options for further actions.
act.double_click(double_click_element).perform()
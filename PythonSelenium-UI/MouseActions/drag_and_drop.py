#Don't run

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop3.html")

time.sleep(4)

#Initiate the double click operation
act = ActionChains(driver)

#elements draggable and drop dest web element location.
sourece_WE = driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b")
dest_WE = driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b")

#after this operation it will show the options for further actions.
#if multiple elements are there then you have to do the same multiple times as we have done below.
act.drag_and_drop(sourece_WE,dest_WE).perform()
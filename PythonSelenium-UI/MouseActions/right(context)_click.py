#Don't run

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Table
driver = webdriver.Chrome()
driver.get("http://swinsl.github.io/jQuery-contextMenu/demo.html")

time.sleep(4)

#Right clickable web element.
web_element = driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b")

act = ActionChains(driver)

#after this operation it will show the options for further actions.
act.context_click(web_element).perform()

#select any one of the option from the right click.
driver.find_element(By.XPATH,value="//span[normalize-space()='copy']").click() # selected the copy option

#Handle the pop up or alert
driver.switch_to.alert.accept()
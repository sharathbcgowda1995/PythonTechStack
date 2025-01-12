import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Table
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH,value="//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,value="//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,value="//*[@id='btnLogin']").click()

time.sleep(4)

#click on admin
admin = driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b")

#click on user management
user_mgmt = driver.find_element(By.ID,value="menu_admin_UserManagement")

#click on the "menu_admin_viewSystemUsers" - click on the disappering element and right click inspect.
menu_admin_viewSystemUsers  = driver.find_element(By.ID,value="menu_admin_viewSystemUsers")

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(user_mgmt).move_to_element(menu_admin_viewSystemUsers).click().perform()

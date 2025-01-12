import time
from selenium import webdriver
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
driver.find_element(By.XPATH,value="//a[@id='menu_admin_viewAdminModule']/b").click()

#click on user management
driver.find_element(By.ID,value="menu_admin_UserManagement").click()

#click on the "menu_admin_viewSystemUsers" - click on the disappering element and right click inspect.
driver.find_element(By.ID,value="menu_admin_viewSystemUsers").click()

#Total number of users is depending up on total number of rows.
#//table[@id='resultTable']/tbody/tr[1]/td[5]
rows_users  = len(driver.find_elements(By.XPATH,value="//table[@id='resultTable']/tbody/tr"))
print("Total number of users are : " ,rows_users)

count = 0
#Print the disabled users from the table.
for user in range(1,rows_users+1):
    status = driver.find_element(By.XPATH,value="//table[@id='resultTable']/tbody/tr["+str(user)+"]/td[5]").text
    if(status=="Disabled"):
        count+=1
        username = driver.find_element(By.XPATH, value="//table[@id='resultTable']/tbody/tr[" + str(user) + "]/td[2]").text
        print("Disabled user name is : ",username)

print("Total number of users are : ",rows_users)
print("Total number of disabled users are : ",count)
print("Total number of enabled users are : ",(rows_users-count))


time.sleep(4)
driver.quit()
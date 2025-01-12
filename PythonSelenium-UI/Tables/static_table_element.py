import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Table
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(4)

#row count
rows =len(driver.find_elements(By.XPATH , value="//table[@name='BookTable']/tbody/tr"))
#col count
column = len(driver.find_elements(By.XPATH,value="//table[@name='BookTable']/tbody/tr[2]/td"))

#print the books of Mukhesh
for row in range(2,rows+1):
    author = driver.find_element(By.XPATH, value="//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[2]").text
    if author == "Mukesh":
        bookname = driver.find_element(By.XPATH,value="//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        price = driver.find_element(By.XPATH,value="//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[4]").text
        print(author,"  ",bookname,"    ",price)

time.sleep(3)
driver.quit()

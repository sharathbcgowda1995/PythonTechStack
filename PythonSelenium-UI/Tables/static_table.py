import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Table
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(4)

#Count the table rows and columns.
row = driver.find_elements(By.XPATH,value = "//table[@name='BookTable']/tbody/tr")
col = driver.find_elements(By.XPATH,value="//table[@name='BookTable']/tbody/tr[1]/th")

print("Number of rows : ",len(row))
print("Number of columns : ",len(col))

#Count all the data
for r in range(2,len(row)+1):
    for c in range(1,len(col)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end=" ")
    print()

time.sleep(3)
driver.quit()
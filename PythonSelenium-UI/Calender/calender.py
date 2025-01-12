import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://jqueryui.com/datepicker/")

month="April"
year="2023"
date="15"

#Inspect the date zone first.
driver.switch_to.frame(0)

#Click on the date picker
driver.find_element(By.XPATH,value="//*[@id='datepicker']").click()

#Search for the "month and year" we are looking for.
while True :
    mon =driver.find_element(By.XPATH,value="//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,value="//span[@class='ui-datepicker-year']").text
    if month==mon and year==yr :
        break
    else :
        driver.find_element(By.XPATH,value="//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

#Select the date after grabbing all the dates and compare by using the if loop(we can use one more logic of rows and col using 2 for loops)
dates = driver.find_elements(By.XPATH,value="//table[@class='ui-datepicker-calendar']//tr/td/a")
for dt in dates:
    if dt.text==date:
        dt.click()
        break

#NOTE
#1.In Travel booking applications we can only select the future dates.
#2.In DOB selection application we will only select the past dates not the future.
###Hence our logic should be implemented accordingly for past or future.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

month="Nov"
year="1995"
date="21"

#Click on the DOB web element.
driver.find_element(By.XPATH,value="//input[@id='dob']").click()

#Select the month from the select class static dropdown.
month_WEBELE = driver.find_element(By.CLASS_NAME,value="ui-datepicker-month")
date_picker_monthSelect = Select(month_WEBELE)
date_picker_monthSelect.select_by_visible_text(month)

#Select the year from the select class static dropdown.
year_WEBELE = driver.find_element(By.CLASS_NAME,value="ui-datepicker-year")
year_picker_yearSelect = Select(year_WEBELE)
year_picker_yearSelect.select_by_visible_text(year)


#Select the date from the table.
dates = driver.find_elements(By.XPATH,value="//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for dt in dates:
    if dt.text == date :
        dt.click()
        break

time.sleep(5)
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://demo.nopcommerce.com/register")

#1.application commands -title,current_url,page_source[We use it directly with the drivers]
print("---------1>application commands -title,current_url,page_source------------")
print('Title is : ',driver.title)
print("Current url is : ",driver.current_url)
print("Page source is : ",driver.page_source)

#1.conditional commands - is_displayed(),is_enabled(),is_selected()[we use it with web elements]
print("---------1>application commands -title,current_url,page_source------------")
#is_displayed-used on we
isDisplayed = driver.find_element(By.ID,value="small-searchterms").is_displayed()
print("Is diplayed : " ,isDisplayed)

#is_selected-used on WE
isEnabled=driver.find_element(By.ID,value="small-searchterms").is_enabled()
print("Is enabled : ",isEnabled)

#is_selected will be used for the checkbox and radio buttons
isSelected = driver.find_element(By.ID,value="gender-male").is_selected()
print("Is selected  : ",isSelected)

#after selection
isSelected = driver.find_element(By.ID,value="gender-male").click()
isSelected = driver.find_element(By.ID,value="gender-male").is_selected()
print("Is selected  after selection  : ",isSelected)



time.sleep(2)
driver.quit()


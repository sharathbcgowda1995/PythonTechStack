import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#Frames
#before we perform anything on the frames first we have to switch to the frame then we can perform the ncessaey actions
driver.get("http://demo.automationtesting.in/Frames.html")

#Switched to parent frame by passing the web element as there is no id and name
driver.find_element(By.XPATH,value="//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)

#Switched to inner frame(Child) by passing the web element
frame=driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe"))
time.sleep(4)

#Written xpath for the inner element to perform some action on it
driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/section/div/div/iframe"))
driver.find_element(By.XPATH,value="/html/body/section/div/div/div/input").send_keys("Hello....")

#Syntax for the switch to frame from sel-3
#driver.switch_to_parent_frame()

time.sleep(4)
driver.quit()
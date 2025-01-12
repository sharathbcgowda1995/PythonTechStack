import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#Frames
#before we perform anything on the frames first we have to switch to the frame then we can perform the ncessaey actions
driver.get("http://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#Frame-1
#we can switch to frames by passing the name,index,webelement,id
driver.switch_to.frame("packageListFrame") #switched to frame by name
driver.find_element(By.LINK_TEXT,value="org.openqa.selenium").click()
driver.switch_to.default_content() #exit from the frame to main page.

time.sleep(2)

#Frame-2
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,value="WebDriver").click()
driver.switch_to.default_content() #exit from the frame to main page.

#Frame-3
#selectorshub won't work properly on the frame
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,value="/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
driver.switch_to.default_content() #exit from the frame to main page.


time.sleep(5)
driver.quit()
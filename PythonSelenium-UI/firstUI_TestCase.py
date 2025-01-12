'''
First test case :
1.open web browser - chrome
2.open URL "https://opensource-demo.orangehrmlive.com/"
3.enter username :
4.enter password :
5.click on login
6.capture title of the home page (Expected)
7.vrify title of the web page (Expected)
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://opensource-demo.orangehrmlive.com/")

#finding the web elements and performing required operaions on them
driver.find_element(by=By.NAME,value="txtUsername").clear() #Need to clear the existing text by this clear method.
driver.find_element(by=By.NAME,value="txtUsername").send_keys("Admin")
driver.find_element(by=By.NAME, value="txtPassword").send_keys("admin123")
#driver.find_element_by_name()-- this is deprecated hence we followed the above process.

#Click on the button
driver.find_element(by=By.ID,value="btnLogin").click()

#validate after successfull login
act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login is succesfull")
else:
    print("Login failed")

#Given some delay to observe the operaions performed
time.sleep(4)

#closed the driver
driver.close()

#*****************************************#
#selenium-4 feature.
"""
from selenium.webdriver.chrome.service import Service
ser_obj=Service("path of the driver")
driver=webdriver.Chrome(service=ser_obj)
"""



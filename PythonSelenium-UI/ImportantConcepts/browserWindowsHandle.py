import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#Frames
#before we perform anything on the frames first we have to switch to the frame then we can perform the ncessaey actions
driver.get("https://opensource-demo.orangehrmlive.com/")

#it returns window id of the one browser window.
single_windowID=driver.current_window_handle
print("Single window id : ", single_windowID)

#now the driver is pointing to the child window
driver.find_element(By.XPATH,value="//a[normalize-space()='OrangeHRM, Inc']").click()

#As we have opened multiple window wec can make use of window_handles() to switch b/w tabs
#It returns the window ID's of the multiple browser window
mul_windowID  = driver.window_handles
parent_window = mul_windowID[0]
child_window = mul_windowID[1]

print("parent id is : ",parent_window)
print("Child id is : ",child_window)

#switch back to the parent window
driver.switch_to.window(parent_window)

#How to switch to the child_tab ??
driver.switch_to.window(child_window)
title = driver.title
print(title)
if title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":
    print("I'm in child window now....")
else:
    print(driver.current_window_handle)

#How to switch to the child_tab ??
driver.switch_to.window(parent_window)

#How to switch to the multiple browser windows.
for win_id in mul_windowID:
    driver.switch_to.window(win_id)
    print(win_id.title())

#How to close the specific browser window.
for close_id in mul_windowID:
    driver.switch_to.window(close_id)
    if(driver.title=="OrangeHRM"):
        driver.close()


time.sleep(4)
driver.quit()
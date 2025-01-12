import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#When I click on the below web element the js window will pop up
element  = driver.find_element(By.XPATH,value="//button[normalize-space()='Click for JS Prompt']")
element.click()

#To handle the js pop up we have to first switch to the js-alerts
js_alert=driver.switch_to.alert

#To get the text of the js alert window.
print(js_alert.text)

#we can pass the values as below we need not to find again the element as we have already switched to the alerts.
js_alert.send_keys("Hii......")

#To click on okay we have accept method.
#js_alert.accept()

time.sleep(5)

#To click on cancel we have dismiss method
#js_alert.dismiss() - we can also directly use as below
driver.switch_to.alert.dismiss()

time.sleep(2)
driver.quit()

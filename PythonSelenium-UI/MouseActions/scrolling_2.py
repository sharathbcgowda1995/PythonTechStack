import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/all-countries.html")
driver.implicitly_wait(10)
driver.maximize_window()

#Give some time to load the page with all the webelement's
time.sleep(3)

#2.Scroll the page till the element is visible.
#JS code to scroll the page.
element  = driver.find_element(By.XPATH,value="//li[normalize-space()='Myanmar']")
driver.execute_script("arguments[0].scrollIntoView();",element)

#To get the total numbers of pixcels moved after above JS code execution
value = driver.execute_script("return window.pageYOffset;")
print("Number pixecels moved : ",value)

time.sleep(3)
driver.close()



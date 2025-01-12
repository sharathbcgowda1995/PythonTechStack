import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

#find the buttons to drap and drop from ato b and b to a ends of sliedr
beg_point = driver.find_element(By.XPATH, value="//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
time.sleep(2)
end_point = driver.find_element(By.XPATH,value="//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")

#to get x axis and y axis location value
print("---------Location of the x and y axis elements before--------")
print(beg_point.location)
print(end_point.location)

actions = ActionChains(driver)

#It's an action class method where we can specify x and y axis value to drag and drop the slider
actions.drag_and_drop_by_offset(beg_point,100,0).perform()
actions.drag_and_drop_by_offset(end_point,-50,0).perform()

print("---------Location of the x and y axis elements before--------")
print(beg_point.location)
print(end_point.location)

time.sleep(5)
driver.quit()
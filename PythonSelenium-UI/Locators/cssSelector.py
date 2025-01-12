#LOCATORS - classname,tagname,css selectors,
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")

#Class name.
sliders = driver.find_elements(By.CLASS_NAME,value="homeslider-container")
print("Total number of sliders are : " , len(sliders))

#Tagname
links = driver.find_elements(By.TAG_NAME,value="a")
print("Total links present are : ",len(links))

#1.CSSSelectors - tag and id tagname#calssvalue
#search_query form-control ac_input -- if the class name has the spaces then consider the one which are separated by spaces.
driver.find_element(By.CSS_SELECTOR,value=".search_query")

#2.CSSSelectors - tag and id tagname#idvalue
driver.find_element(By.CSS_SELECTOR,value="#index").click()

time.sleep(3)

#3.CSSSelectors - Tag and Attribute -- tagname[attribute=attributeValue]
driver.find_element(By.CSS_SELECTOR,value="img[alt='Logo Google']")

time.sleep(3)

#4.CSSSelectors - Tagname , classname and attribute
#tagname.classname[attribute='attributevalue'] -- we write in this way when this combo has multiple values tagname.classname
#driver.find_element(By.CSS_SELECTOR,value="img.lazyloaded[alt='Logo Google']") #this is how we write but commented as it's notworking


time.sleep(3)
driver.close()

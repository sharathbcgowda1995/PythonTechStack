import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url to open the web applications on the same tab.
driver.get("https://www.amazon.com/")

print("-----------find_element()-------------")

#difference between find_element and find_elements
#1.returns only one element which occurs first from left to right even though the locator is pointing to multiple elements.
element = driver.find_element(By.XPATH,value="//span[@class='nav-line-1']")
print(element.text)

#2.If we pass the wrong locator then it returns the "no such element exception"
try:
    driver.find_element(By.LINK_TEXT,value="Todayjhswiusg Deals")
except NoSuchElementException :
    print("No such element exception handled")

#3 It returns only on element.
element= driver.find_element(By.LINK_TEXT,value="Today's Deals")
print(element.text)

print("-----------find_elements()-------------")

#1.driver.find_elements()- it will return the multiple list of elements.
elements = driver.find_elements(By.XPATH,value="//span[@class='nav-line-1']")
print("Length of the returned elements is : ",len(elements))

#2.when we pass the locator which points to only one element then it returns that element as a first element of the list.
elements = driver.find_elements(By.LINK_TEXT,value="Today's Deals")
print("length with one WE locator : " ,len(elements) ,"And element is :",elements[0].text)

#3.when we pass the invalid locator to find_elements it won't actually throw the error instead it returns the empty array.
elements = driver.find_elements(By.XPATH, value="//a[@class='1234bh']")
print("Checking the length when we pass the wrong locator : ",len(elements))

time.sleep(3)
driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("https://itera-qa.azurewebsites.net/home/automation")

#1.selection of single checkbox
driver.find_element(By.ID,value="tuesday").click()
print("Is selected ? : ",driver.find_element(By.ID,value="tuesday").is_selected())

#2.To unclick the element click on the same element.
driver.find_element(By.ID,value="tuesday").click()

#3.Select days related checkboxes
print("----------days related checkboxes are clicked-----------")
elements = driver.find_elements(By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
for element in elements:
    element.click()
#Other way of clicking
#for i in range(len(elements)):
#   elements[i].click()

#4.To check whether all of those are selected or not
print("------check the selection by using is_selected() method-------")
for element in elements:
    print(element.is_selected())

#5.How to uncheck all again ? clicking on it again.
print("------clicked elements are unclicked-----------")
elements = driver.find_elements(By.XPATH,value="//input[@type='checkbox' and contains(@id,'day')]")
for element in elements:
    element.click()

print("------check the selection by using is_selected() method-------")
for element in elements:
    print(element.is_selected())

#6.select the first two elements from the check list - 0th,1st element
print("--------first two elements are clicked---------")
for i in range(len(elements)):
    if i<2:
        elements[i].click()
        print(elements[i].get_attribute("id")," element clicked ")
#unclick the last two elements by clickin on them again
for i in range(len(elements)):
    if i<2:
        elements[i].click()
        print(elements[i].get_attribute("id")," element clicked to uncheck")

#7.select the last two elements .
print("-----last two elements are clicked--------")
for i in range(len(elements)-2,len(elements)):
    elements[i].click()
    print(elements[i].get_attribute("id"), " element clicked ")


time.sleep(10)
driver.quit()
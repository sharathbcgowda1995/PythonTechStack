import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("http://www.opencart.com/index.php?route=account/register")
time.sleep(15)

#Dropdown - selecting the element form the dropdown
#1.write the locator for the element which has multiple elements
#usually the dropdowns has select tag
select_tag_element = driver.find_element(By.ID,value="input-country")

#2.Pass the web element to select calss
select_class_element = Select(select_tag_element)

#3.we have different methods to select the web element we want.
select_class_element.select_by_visible_text("India") #case sensitive.
#select_element.select_by_value("13") #Australia need to be selected.
#select_element.select_by_index(2) #Albania needs to be selected

#--How to count all the dropdown options.
print("---------printed all the dropdown option count-------")
allOptions = select_class_element.options #it gives all the web element options of dropdown
print("The total options are : ", len(allOptions))

#How to print them ? using for loop
print("------All the options are displayed here----------")
for option in allOptions:
    print(option.text)

#How to select the web elements without using the above mentioned built in functions ????
for option in select_class_element:
    if(option.text)=="India":
        option.click()

#if select class is not there for the dropdown then we can write generic xpath for all the options,forloop iteration , if cond ,click
option_ele = driver.find_elements(By.XPATH,value="//select[@id='input-country']/option") #/option  pointing all that options.
print(len(option_ele))
for opt in option_ele:
    if(opt.text)=="India":
        option.click()

time.sleep(15)
driver.quit()
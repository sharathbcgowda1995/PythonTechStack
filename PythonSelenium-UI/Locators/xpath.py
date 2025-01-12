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

#Click on the button
driver.find_element(by=By.ID,value="btnLogin").click()

#xapth
#we can use any type of the attribute as per written synatx , for ex i have used id but for id we directly go with that locator it self
xpathVal=driver.find_element(By.XPATH,value="//a[@id='menu_buzz_viewBuzz']").text
print("normal syntax x-path : ",xpathVal)

#and
#Both should be on web page then only it will be verified
andVal=driver.find_element(By.XPATH,value="//input[starts-with(@ id,'MP_l') or @value='Marketplace']")
print("and used ----",andVal.text)

#and
#if anyone broken also it will be identified with one more.Both should be uniqiely identifiable to single element.
#//input[@type='button' and @value='Marketplace'] -- This type also possible.
orVal=driver.find_element(By.XPATH,value="//input[@class='button'and @value='Marketplace']").text
print("or used --- ",orVal)

#contains(@attribute,'attributeval')
#If some locators are changing dynamically but if they have some common letters in that --ex:start/stop-- is a name of that attribute
#then we can use st[ ts , sr -- it's correcy if changed element also has this] - any common from which to which state it changes
contVal=driver.find_element(By.XPATH,value="//input[contains(@ id,'MP_link')]").text
print("Contains method -- ",contVal)

#starts-with(@attribute,'attributeval')
#id='MP_link' we can use MP_l or MP_li -- it should be same as first letters if attr value
startsWithtVal=driver.find_element(By.XPATH,value="//input[starts-with(@ id,'MP_l')]").text
print("Contains method -- ",startsWithtVal)
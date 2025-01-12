import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#self-slef - //tagname[@attribute="attributeValue"]/self::selfTagName
valueOfTheSelfElement = driver.find_element(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/self::a")
print(valueOfTheSelfElement.text)

#self-parent - //tagname[@attribute="attributeValue"]/parent::parentTagName
valueOfTheParentElemnt = driver.find_element(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/parent::td")
print(valueOfTheParentElemnt.text)

#self-ancestor #self-parent-ancestor - //tagname[@attribute="attributeValue"]/ancestor::ancesstorTagName -- [/parent::td/ancestor::tr]possible
valueOfTheAnsestorElement = driver.find_element(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/ancestor::tr")
print(valueOfTheAnsestorElement.text)#we can directly go to the ancestor element by skipping the parent

#self-ancestor-child - //tagname[@attribute="attributeValue"]/ancestor::ancesstorTagName/child::childTagName
elementsOfTheRow = driver.find_elements(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/ancestor::tr/child::td")
print(len(elementsOfTheRow))

print("-------Iterate over the row elements--------")
for element in range(len(elementsOfTheRow)):
    print(elementsOfTheRow[element].text)

#ancestor(node)-descendant
#To find all the descendant elements put * at descendant tag place which will returns the list of web elements
#//a[normalize-space()='Zensar Technologies']/ancestor::tr/descendant::*
descendantValue = driver.find_element(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/ancestor::tr/descendant::a")
print(descendantValue.text)
#print(descendantValue.__getattribute__("href"))



#########-------need to check this part----------------------_#########

#self-preceding(refer notes)- above elements are preceding
precedingElementCount = driver.find_elements(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/preceding::*")#* or preceding tag names
print(len(precedingElementCount))

#self-following(refer notes) below the self elements are the following
followingElementCount = driver.find_elements(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/following::*")#* or following tag names
print(len(followingElementCount))

#self-[preceding-sibling](refer notes)- above elements are preceding
precedingSiblingElementCount = driver.find_elements(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/preceding-sibling::*")#* or preceding tag names
print(len(precedingSiblingElementCount))

#self-[following-sibling](refer notes) below the self elements are the following
followingSiblingElementCount = driver.find_elements(By.XPATH,value="//a[normalize-space()='Zensar Technologies']/following-sibling::*")#* or following tag names
print(len(followingSiblingElementCount))


time.sleep(3)
driver.quit()

import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Trigger the driver
driver=webdriver.Chrome()   #executable_path="path of the driver present can passed here"

#passing the url
driver.get("http://deadlinkcity.com")

#1.internal link - after we click on the link we will be on the same page.
#2.external link - new web page in new window it will open
#driver.find_element(By.LINK_TEXT,value="Comparison Table.").click()

#Capture the broken links.
#3.Gather all the links from the web page
#all_links = driver.find_element(By.TAG_NAME,value="a")
all_links = driver.find_elements(By.XPATH,value="//a")
total_links=len(all_links)
print("Total  number of links : ",total_links)

#extra for my knowledge
#Keep an counter to count both active and broken links:
broken_link_count = 0
active_links = 0

##IMP
#iterate the web elements using for loop and capture the attribute href for the url and pass it in get
for link in all_links:
     url =   link.get_attribute("href")
     try:
            response = requests.head(url)
            if response.status_code >= 400:
                print(url, "Link is broken")
                broken_link_count = broken_link_count + 1
            else:
                print(url, "links is active")
                active_links = active_links + 1
     except :
            None

##extra for my knowledge
#prin the count of active and broken
print("Number of active links are : " ,active_links)
print("Number of broken links are : ",broken_link_count)

#finally after all the count, we can add active+broken to check whether it matches with the total link or not.
print("Sum of two are : ", (broken_link_count+active_links))

if total_links==(broken_link_count+active_links):
    print("All the links has been checked")
else:
    print('some of the links are missing as the total link is missing.....')

time.sleep(5)
driver.quit()
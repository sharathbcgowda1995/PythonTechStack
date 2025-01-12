import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

#Trigger the driver
driver=webdriver.Chrome(options=opt)   #executable_path="path of the driver present can passed here"

#Frames
#before we perform anything on the frames first we have to switch to the frame then we can perform the ncessaey actions
driver.get("https://www.gps-coordinates.net/my-location")

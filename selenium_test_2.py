from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\user\PycharmProjects\Test\drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)

print(driver.title)

driver.back()

time.sleep(5)

print(driver.title)

driver.forward()

time.sleep(5)

print(driver.title)
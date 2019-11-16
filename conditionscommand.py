from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\user\PycharmProjects\Test\drivers\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name('userName')

print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name('password')

print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys('mercury')
pwd_ele.send_keys('mercury')

driver.find_element_by_name('login').click()

roundtrip_radio=driver.find_element_by_css_selector('input[value=roundtrip]')
print("status of round trip round button", roundtrip_radio.is_selected())

oneway_radio=driver.find_element_by_css_selector('input[value=oneway]')
print("status of one way round button", oneway_radio.is_selected())


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\Test\drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.find_element_by_name('q').send_keys("Facebook Login", Keys.ENTER)

time.sleep(20)
driver.quit()

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\user\PycharmProjects\Test\drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.find_element(By.ID,"tab-flight-tab-hp").click()

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

time.sleep(2)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("15/10/2018")

driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

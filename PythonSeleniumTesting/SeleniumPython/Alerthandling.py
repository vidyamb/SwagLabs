import time

from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

driver.find_element_by_id("name").send_keys("Vidya")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
alert.accept()

driver.find_element_by_id("name").send_keys("Vidya")
driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
alert.accept()
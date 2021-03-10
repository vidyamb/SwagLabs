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
#driver.back()
#driver.refresh()
#driver.minimize_window()
#driver.close()


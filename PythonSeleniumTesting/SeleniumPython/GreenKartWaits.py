import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

#driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
list=[]
list1=[]
#driver.find_element_by_xpath("//button[@type='submit']")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
assert count==3


buttons=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#wait=WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "input.promoCode")))

veggies = driver.find_elements_by_xpath("//tr/td[2]/p")
for veg in veggies:
    list1.append(veg.text)
print(list1)

assert list == list1
print("both products matches")

TA_beforeDiscount = driver.find_element_by_css_selector(".discountAmt").text
print(TA_beforeDiscount)

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button.promoBtn")))
driver.find_element_by_css_selector("button.promoBtn").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)


TAafterdiscount = driver.find_element_by_css_selector(".discountAmt").text
print(TAafterdiscount)

assert float(TAafterdiscount) < int(TA_beforeDiscount)

amounts= driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

assert int(TA_beforeDiscount) == sum







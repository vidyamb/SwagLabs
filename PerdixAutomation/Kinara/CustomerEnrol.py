import time

from select import select

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.implicitly_wait(10)
driver.get("https://uat-kinara.perdix.co.in/perdix-client/#/Page/Engine/")

print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_id("inputEmail3").send_keys("ayush")
driver.find_element_by_id("inputPassword3").send_keys("PAss@1234")
driver.find_element_by_xpath("//button[@type='button']").click()

wait = WebDriverWait(driver, 50)
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//body/ui-view[1]/div[1]/aside[1]/section[1]/ul[1]/li[3]/a[1]')))
driver.find_element_by_xpath("//body/ui-view[1]/div[1]/aside[1]/section[1]/ul[1]/li[3]/a[1]").click()
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, "//section/ul[@class='sidebar-menu']/li[3]/ul/li[2]/a")))

indvCustom = driver.find_element_by_xpath("//section/ul[@class='sidebar-menu']/li[3]/ul/li[2]/a")
time.sleep(5)
ActionChains(driver).move_to_element(indvCustom).click(indvCustom).perform()
time.sleep(5)
branchName = Select(driver.find_element_by_css_selector("#customerBranchId"))
branchName.select_by_visible_text("Head Office")
time.sleep(3)
spokeName = Select(driver.find_element_by_id("centreId"))
spokeName.select_by_index(1)
time.sleep(3)
gallery = driver.find_element_by_xpath("//div[@id='PERSONAL_INFORMATION']//div//button")
gallery.send_keys("C:\\Users\\vidya\\Downloads\\image.jpg")
# driver.back()
# driver.refresh()

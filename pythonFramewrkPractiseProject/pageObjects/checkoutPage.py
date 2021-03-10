from itertools import product

from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkOut = (By.CSS_SELECTOR, "//div[@class='card h-100']")

    def Card(self):
        self.driver.find_elements(*CheckoutPage.checkOut).click()
        return


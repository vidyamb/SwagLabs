from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='/angularpractice/shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_elements(*HomePage.shop).click()
        checkoutPage=CheckoutPage(self.driver)
        return CheckoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_elements(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertmessage(self):
        return self.driver.find_element(*HomePage.successMessage)


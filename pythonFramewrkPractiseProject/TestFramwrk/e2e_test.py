from lib2to3.pgen2 import driver

import products as products
import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utility.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.checkoutPage import CheckoutPage


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_first(self):

        self.driver.implicitly_wait(10)
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        # self.driver.find_element_by_css_selector("a[href*='/angularpractice/shop']").click()
        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.Card().click()

        #driver.find_elements_by_xpath("//div[@class='card h-100']")

        products = self.driver.find_elements_by_xpath("a[href*='/angularpractice/shop']")

        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text

        if productname == "Blackberry":
            product.find_element_by_xpath("div/button[@class='btn btn-info']").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        self.driver.find_element_by_css_selector("#country").send_keys("ind")
        self.VerifyLinkpresence("India")
        self.driver.find_element_by_xpath("//a[text()='India']").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[value*='Purchase']").click()


        print(self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

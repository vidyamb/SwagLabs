from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utility.BaseClass import BaseClass
from pageObjects.Homepage import HomePage


class TestHomepage(BaseClass):

    def test_formSubmission(self):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getmail().send_keys(getData[1])
        homepage.getCheck().click()

        # self.SelectOptionsBytext(homepage.getGender(), "Male")
        # homepage.getGender().click
        homepage.submitForm().click()

        #homepage.getAlertmessage().text
        print("alertmessage")

        # assert ("Success" in msg)

  #@pytest.fixture(params=[("rahul", "shetty"), ("manish", "shet")])
    #def getData(self, request):
        #return request.param

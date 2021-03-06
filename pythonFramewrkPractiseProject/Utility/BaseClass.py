import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Homepage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass



    def VerifyLinkpresence(self, text):
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionsBytext(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

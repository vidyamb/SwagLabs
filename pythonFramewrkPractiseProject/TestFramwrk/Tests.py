import pytest

from Utility.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_one1(self):
        self.driver.find_element_by_id("name").click()

print("Hello")

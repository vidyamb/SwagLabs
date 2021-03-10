import pytest

@pytest.mark.usefixtures("setUp")
class TestExample:

    def test_fixtureDemo1(self):
        print("i wll execute in this method")

    def test_fixtureDemo2(self):
        print("i wll execute in this method")

    def test_fixtureDemo3(self):
        print("i wll execute in this method")




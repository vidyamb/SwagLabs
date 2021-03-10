import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_edit_profile(self, dataLoad):
        print(dataLoad)
import pytest


@pytest.fixture(scope='class')
def setUp():
    print("I will execute first")
    yield
    print("i will execute at last")


@pytest.fixture()
def dataLoad():
    print("data loading from here")
    return['rahul', 'shetty', 'academy.com']

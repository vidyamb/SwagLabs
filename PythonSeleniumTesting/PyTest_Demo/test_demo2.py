import pytest


def test_secondprogram():
    msg="hello"
    assert msg == "hello" , "message do not matches"

@pytest.mark.smoke
def test_program():
    a=5
    b=7
    assert a+3==8 ," addition not matches"

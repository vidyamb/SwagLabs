import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    print("Miss u bappa")

@pytest.mark.xfail
def test_firstprogram1():
    print("Good morning")


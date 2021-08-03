import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello Pytest!!!")

@pytest.mark.xfail
def test_secondProgram_creditcard():
    print("Welcome!!!")
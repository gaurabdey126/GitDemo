import pytest


@pytest.mark.smoke
def test_thirdProgram():
    msg = "Maldives"
    assert msg == "Europe", "The Strings are not matching"  ## Extra text is given to produce in assertion error

@pytest.mark.skip
def test_fourthProgram_creditcard():
    a = 4
    b = 6
    assert a+2 == 6
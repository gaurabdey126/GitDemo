import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setup")
class Test:
    def test_fixture1(self):  ### only self as we are not calling any data
        print("This is the Website for Practice111111")

    def test_fixture2(self):
        print("This is the Website for Practice22222222")

    def test_fixture3(self):
        print("This is the Website for Practice3333333")
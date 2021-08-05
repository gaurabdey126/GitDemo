# @pytest.mark.usefixtures("setup")  ### this is commented as Utilities BaseClass is called by inheritance which is in turn calling usefixture
import allure
import pytest
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass  ## from <package>.<filename> import <class name>
from pageObjects.HomePage import HomePage  ## from <package>.<filename> import <class name>
from TestData.HomePageData import HomePageData


class TestFormSubmission(BaseClass):

    @allure.description("Form Submission flow")
    @allure.severity(severity_level="CRITICAL")
    def test_formSubmission(self, getData):   ### getData method is included to get the data from that method
        log = self.getLog()
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData["Name"])  ## using Dictionary Data type but for both we have to pass the getData method in main method
        # homepage.getName().send_keys(getData[0])  ## using tuple data type

        homepage.getEmail().send_keys(getData["Email"])  ## using Dictionary Data type
        # homepage.getEmail().send_keys(getData[1]) ## using tuple data type

        homepage.getCheckbox1().click()
        homepage.getRadio2().click()

        # dropdown = Select(homepage.getGender())   #from selenium.webdriver.support.select import Select
        # dropdown.select_by_index(1)
        # self.dropdownOptionbyText(homepage.getGender(), getData[2])  ##locator, text  ## using tuple data type
        self.dropdownOptionbyText(homepage.getGender(), getData["Gender"])  ##locator, text  ## using Dictionary Data type

        homepage.getSubmit().click()
        print(homepage.getSuccess().text)
        log.info(homepage.getSuccess().text) ## logger

        assert "Success!" in (homepage.getSuccess().text)

        print("Form has been submitted successfully BY THE USER")
        self.driver.refresh()           ### this is must as we are entering the data multiple time

    # this fixture with param is necessary if we are feeding multiple data in the same place

    # TUPLE DATA TYPE
    # @pytest.fixture(params=[("Gaurab", "abc@gmail.com", "Male"), ("Ethan", "hunt@gmail.com", "Female"),("Bond", "James@hotmail.com", "Female")])  ### params= is a must and it should hold the multiple data
    # DICTIONARY DATA TYPE is HomePageData
    @pytest.fixture(params= HomePageData.getTestData("test case 5"))  ## calling the HomePageData class and then it variable as class.variable
    def getData(self, request):  ### request argument is manadatory
        return request.param


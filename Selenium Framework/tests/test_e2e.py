import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
# @pytest.mark.usefixtures("setup")  ### this is commented as Utilities BaseClass is called by inheritance which is in turn calling usefixture
import allure
from utilities.BaseClass import BaseClass  ## from <package>.<filename> import <class name>
from pageObjects.HomePage import HomePage  ## from <package>.<filename> import <class name>
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage

class TestOne(BaseClass):

    @allure.description("E2E flow of Buying")
    @allure.severity(severity_level="HIGH")
    def test_e2e(self):       ### need to pass the fixture method as argument
        log = self.getLog()         ### calling and mapping the LOG here which is there in the BaseClass
        homepage = HomePage(self.driver)  ### assigning an OBJECT to the class created in POM pages(heres, Homepage)
        homepage.shopItems().click()  ### with the newly created object, I am calling the method which is having the XPATH for the same

        checkoutpage = CheckoutPage(self.driver)
        products = checkoutpage.getProducts()

        i = -1
        for product in products:
            i = i + 1
            product_brand = product.text
            print(product_brand)
            log.info(product_brand) ## we can use log instead of Print
            if product_brand == "Nokia Edge":
                checkoutpage.getAdd()[i].click()

        checkoutpage.checkout1().click()
        assert checkoutpage.getProdlist().text == 'Nokia Edge'
        # print("Product is same between Add and Checkout page")
        log.info("Product is same between Add and Checkout page")  ## we can use log instead of Print

        checkoutpage.checkout2().click()

        confirmpage = ConfirmPage(self.driver)
        log.info("Enter the value as Ind")
        confirmpage.getCountry().send_keys("Ind")

        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")  ### calling the method from BaseClass where explicit wait is given with argument as text
        confirmpage.selectCountry().click()

        confirmpage.selectCheckbox().click()
        confirmpage.purchaseButton().click()
        success_msg = confirmpage.success_MSG().text
        assert "Success!" in success_msg

        # assert "Hello!" in success_msg ## to check allure screenshot functionality
        # if AssertionError:
            # allure.attach(confirmpage.get_screenshot_as_png(), name="Error SS", attachment_type=allure.attachment_type.PNG)

        print(success_msg)
        # # self.driver.get_screenshot_as_file("screen.png")

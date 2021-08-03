from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    selectcountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CLASS_NAME, "btn-success")
    success_message = (By.CSS_SELECTOR, ".alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectcountry)

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def success_MSG(self):
        return self.driver.find_element(*ConfirmPage.success_message)
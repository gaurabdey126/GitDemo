from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):  ## constructor is used as we have to call the driver...always n befor any method is called
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']") ##self.driver.find_element_by_css_selector("a[href*='shop']").click()
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    check1 = (By.ID, "exampleCheck1")
    rad2 = (By.XPATH, "//input[@id='inlineRadio2']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit_btn = (By.CSS_SELECTOR, "input[type='submit']")
    success_msg = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)  ### *Classname.variable
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getCheckbox1(self):
        return self.driver.find_element(*HomePage.check1)
    def getRadio2(self):
        return self.driver.find_element(*HomePage.rad2)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit_btn)
    def getSuccess(self):
        return self.driver.find_element(*HomePage.success_msg)

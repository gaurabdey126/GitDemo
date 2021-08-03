from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # prod = (By.XPATH, "//div[@class='card h-100']")  #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    prod = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    # prodname = (By.XPATH, "//div[@class='card h-100']/div/h4/a")  # //div[@class='card h-100']/div/h4/a

    addbutton = (By.XPATH, "//div[@class='card h-100']/div/button")
    # addbutton = (By.XPATH, "//button[@class='btn btn-info']")
    # addbutton = (By.XPATH, "//div[@class='card h-100']/div/h4/a//following::button")

    # prod = (By.XPATH, "//div[@class='card h-100']/child::div/h4")
    # addbutton = (By.XPATH, "//div[@class ='card h-100']/child::div/following-sibling::div/button")  #//div[@class ='card h-100']/child::div/following-sibling::div/button

    checkoutbutton1 = (By.CSS_SELECTOR, ".btn-primary")
    prodlist = (By.XPATH, "//tr/td/div/div/h4/a")
    checkoutbutton2 = (By.CSS_SELECTOR, ".btn-success")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.prod)  ###### *Classname.variable

    # def getProduct(self):
    #     return self.driver.find_element(*CheckoutPage.prodname)

    def getAdd(self):
        return self.driver.find_elements(*CheckoutPage.addbutton)

    def checkout1(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton1)

    def getProdlist(self):
        return self.driver.find_element(*CheckoutPage.prodlist)

    def checkout2(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton2)



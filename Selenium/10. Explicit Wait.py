# This EXPLICIT wait is used to target only specific element. This will not have effect on any other element/object

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")

add_to_cart = driver.find_elements_by_xpath("//div[@class='product']/div/button")  ### tking common xpath for iteration
print("Items listed:", len(add_to_cart))
assert len(add_to_cart) == 3

for i in add_to_cart:
    i.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

#EXPLICIT WAIT
wait = WebDriverWait(driver,5)   ### need to pass 2 arguments...driver itself and wait time in secs
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))  ### .clickable mode and many other are there after expected condition
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
code_success = driver.find_element_by_xpath("//span[text()='Code applied ..!']").text

print(code_success)

### this is extra code written to test
if "Code applied ..!" in code_success:
    print("Test Pass")
else:
    print("Test Fail")



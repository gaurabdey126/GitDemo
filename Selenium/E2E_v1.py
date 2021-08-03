# Selecting a specific brand mobile phone and competing the process and the capturing the success message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    product_brand = product.find_element_by_xpath("div/h4/a").text  #//div[@class='card h-100']/div/h4/a.....a portion of XPATH used as it is navigating from products..
    print(product_brand)
    if product_brand == "Samsung Note 8":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector(".btn-primary").click()
assert driver.find_element_by_xpath("//tr/td/div/div/h4/a").text == 'Samsung Note 8'
print("Product is same between Add and Checkout page")

driver.find_element_by_css_selector(".btn-success").click()
driver.find_element_by_id("country").send_keys("Ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
# assert driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").is_selected()
# print("Checkbox is selected...")

driver.find_element_by_class_name("btn-success").click()
success_msg = driver.find_element_by_css_selector(".alert-success").text

assert "Success!" in success_msg
print(success_msg)
driver.get_screenshot_as_file("screen.png")
driver.close()


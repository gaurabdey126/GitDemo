import time

from selenium import webdriver

list1 = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)   ######IMPLICIT wait applied for 5 secs...GLOBALLY
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_xpath("//input[@type='search']").send_keys("br")

add_to_cart = driver.find_elements_by_xpath("//div[@class='product']/div/button")  ### taking common xpath for iteration
print("Items listed:", len(add_to_cart))
# assert len(add_to_cart) == 3

## //div[@class='product']/div/button/parent::div/parent::div/h4   -->>> complete XPATH...we r taking half XPATH as the current node is in add_to_cart as we are using button.

for button in add_to_cart:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)  ### appending the text in the list1....XPATH continuation after button
    button.click()
print("list1: ",list1)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements_by_xpath("//p[@class='product-name']")

for veg in veggies:
    list2.append(veg.text)
print("List2: ", list2)

list3 = list(filter(None, list2))  ####  to remove extra spaces from list2
print("List3: ", list3)

assert list1 == list3
print("Items are matching in both the pages")

# ORIGINAL AMOUNT
originalAmount = driver.find_element_by_class_name("discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

code_success = driver.find_element_by_xpath("//span[text()='Code applied ..!']").text
print(code_success)

# DISCOUNTED AMOUNT
discountAmount = driver.find_element_by_class_name("discountAmt").text

assert float(discountAmount) < float(originalAmount)
print("Discounted Amount is ", discountAmount, "whereas the Original Amount was ", originalAmount)

driver.close()
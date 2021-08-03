# Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception. This we will set.
# Once this time is set, WebDriver will wait for the element before the exception occurs.
# Once the command is in place, Implicit Wait stays in place for the entire duration for which the browser is open.
# Implicit wait given once will be used for the complete set of code in that.

# This is mostly used when we know that the Application that we are Testing is not superfast and there could be delay for few seconds in loading the objects/page
# Basically it set wait for the Driver Object. So that wait is applied GLOBALLY until your test execution is DONE.
# That means this applicable for each and every step of our Test file.
# Beauty of this WAIT is....If the application loads in less that 5 secs, it will not keep waiting and will proceed immediately..MAX wait=5secs

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)   ######IMPLICIT wait applied for 5 secs...GLOBALLY
driver.get("https://rahulshettyacademy.com/seleniumPractise")

driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")

add_to_cart = driver.find_elements_by_xpath("//div[@class='product']/div/button")  ### tking common xpath for iteration
print("Items listed:", len(add_to_cart))
assert len(add_to_cart) == 3

for i in add_to_cart:
    i.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")


driver.find_element_by_css_selector("button.promoBtn").click()

code_success = driver.find_element_by_xpath("//span[text()='Code applied ..!']").text


### this is extra code written to test
if "Code applied ..!" in code_success:
    print("Test Pass")
else:
    print("Test Fail")



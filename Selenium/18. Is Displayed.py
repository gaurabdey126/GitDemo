from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element_by_id("displayed-text").is_displayed()
print(driver.find_element_by_id("displayed-text").is_displayed())

driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
print(driver.find_element_by_id("displayed-text").is_displayed())

driver.close()

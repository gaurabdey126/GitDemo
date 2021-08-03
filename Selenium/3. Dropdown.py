from selenium import webdriver
from selenium.webdriver.support.select import Select   ###### need to import if Select class is used

driver = webdriver.Chrome(executable_path= "C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("Gaurab")  ### use " " double everywhere or else xpath and css shoes error
driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@id='inlineRadio2']").click()

dropdown = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_value_text("Female")
# dropdown.select_by_index(1)


driver.find_element_by_css_selector("input[type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)


# #Select is a class already present in slenium...but this will work only if the drop down tag ia having SELECT
# dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# dropdown.select_by_value_text("Female")   ### it will select the text visible in the dropdown
# # dropdown.select_by_index(1)  ### it will select the text based on the index number


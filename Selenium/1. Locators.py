from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("Gaurab")  ### use " " double everywhere or else xpath and css shoes error
driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@id='inlineRadio2']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)   #### XPATH = //*[contains(@class,'alert-success')]
# print (driver.find_element_by_css_selector("div[class*='alert-success']").text) ## * means u dont have to write the complete..some part is good enough
driver.close()

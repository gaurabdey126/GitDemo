from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Hello World!!!")
print(driver.find_element_by_name("name").text)              #### this will not return the extered text
print(driver.find_element_by_name("name").get_attribute("value")) ### this will return the entered text with .get_attribute("value")
## JavaScript executor for getting the value:
print(driver.execute_script('return document.getElementsByName("name")[0].value')) ## this is the JavaScript method when Selenium is not able to get the value

##JavaScript executor for clicking an object:

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)  ### arguments with 0 as there is only one object(shopButton)...if more than one then we have to increase it

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  #### scrolling the page to the complete page height
time.sleep(5)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
time.sleep(5)

driver.close()


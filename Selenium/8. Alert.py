from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

entertext = 'Goldberg'
driver.find_element_by_css_selector("#name").send_keys(entertext)  ## locator used is CSS by ID
driver.find_element_by_id("alertbtn").click()

alert = driver.switch_to.alert  ### switching the driver to alert and storing this as an alert variable
print(alert.text)  ### getting the text from the alert
alertText = alert.text
assert entertext in alertText ### validating the entered name is there in the Alert Text or not through Assert
alert.accept()  ### clicks on positive option (yes, Accept, Ok, etc)
# alert.dismiss()   ### clicks on negative option (no, cancel, etc.)
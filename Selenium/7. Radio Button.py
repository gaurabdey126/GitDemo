from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

## We cannot use loop as at once only one radio button can be selected...
radiobutton = driver.find_elements_by_name("radioButton")
print(len(radiobutton))
radiobutton[1].click()

driver.close()
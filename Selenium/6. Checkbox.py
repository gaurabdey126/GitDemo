from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

                                ## storing the coomon checkbox XPATH in a variable which can be used in Loop for iteration
checkboxes = driver.find_elements_by_xpath("//fieldset//child::input[@type='checkbox']")
print(len(checkboxes))  ## getting the count of checkboxes in the page
for i in checkboxes:
    print(i.get_attribute('value'))  ### this can be ignored....
    if i.get_attribute('value')=='option2':   ### to select a particular checkbox....
        i.click()
        assert i.is_selected()  ## .is_selected is used to verify wether the CHECKBOXES in the UI is checked or not...Assertion Error if not selected in UI
driver.close()
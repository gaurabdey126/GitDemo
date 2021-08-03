from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")

driver.find_element_by_link_text("Multiple Windows").click()
driver.find_element_by_xpath("//a[text()='Click Here']").click()

driver.window_handles   #### this stores all the windows coming up in the page in a LIST and then we have to give indexing to call the proper window
## parent window is always at index[0] and then comes the child window at [1], [2], etc...
parentwindow = driver.window_handles[0]
childwindow1 = driver.window_handles[1]

driver.switch_to.window(childwindow1)  ### switching to child window from parent window with proper argument
print(driver.find_element_by_tag_name("h3").text)
driver.close()

driver.switch_to.window(parentwindow) ### switching back to parent window after the child window is closed
print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
print("True")
driver.close()
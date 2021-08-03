from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

#frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")  ### need to pass argument, which frame and that should we get by using frame id/frame name/frame index value. Used Frame name here
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to AUTOMATE !!!!!!!!!")
driver.switch_to.default_content()  ### it will take the driver to main HTML Page again

print(driver.find_element_by_tag_name("h3").text)
driver.close()

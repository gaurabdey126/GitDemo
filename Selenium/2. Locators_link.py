from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get('https://login.salesforce.com')

driver.find_element_by_class_name("username").send_keys('Test1') ##classname locator
driver.find_element_by_css_selector("#password").send_keys("1234") ## css by id...syntax "tagname#Id value"..this works only for ID
driver.find_element_by_css_selector("#password").clear()
driver.find_element_by_css_selector(".username").clear()        ##### css by classname...syntax "tagname.classname value"..this works only for classname
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//input[@name='cancel']").click()

driver.find_element_by_class_name("username").send_keys('Test2')
print(driver.find_element_by_xpath("//form[@name='login']//descendant::label").text) ###XPATH with grandparent child mechanism..it should have / in betn
print(driver.find_element_by_css_selector("form[name='login'] label[for='password']").text) ## CSS with grandparent child mechanism ..it should have space in betn
# form[name='login'] label:nth-child(1)
driver.close()




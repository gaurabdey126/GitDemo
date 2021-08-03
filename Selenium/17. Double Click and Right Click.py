from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()

action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


driver.find_element_by_xpath("//input[@name='prompt']").click()
alert1 = driver.switch_to.alert
alert1.send_keys("Hello Prompt!!!!!!")
alert1.dismiss()






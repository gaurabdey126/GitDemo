import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

### ActionChains is a class that handles mouse hover, rightclick, double click, etc
action = ActionChains(driver)   ### passing the driver as argument...i.e. now action will work on top of driver

menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()   ##### after action., it will just be hover on top of the object identified in menu
## .perform() is always manadtory to make the action works...

childMenu = driver.find_element_by_link_text("Top")  ##### move to element will make the cursor move to the below element identified by locator
action.move_to_element(childMenu).click().perform() ### .click() as we are clicking the option from the hover option


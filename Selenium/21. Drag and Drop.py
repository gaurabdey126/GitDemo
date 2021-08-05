from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.get("https://chercher.tech/practice/drag-drop");
# box1 = driver.find_element_by_css_selector("#box1")
# place1 = driver.find_element_by_id("destination")
# actions = ActionChains(driver)
# # actions.drag_and_drop(box1, place1).click().perform()
# actions.click_and_hold(box1).move_to_element(place1).release(place1).perform()

driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html");
src = driver.find_element_by_xpath("//span[text()='Draggable 3']")
des = driver.find_element_by_id("mydropzone")

action = ActionChains(driver)
action.drag_and_drop(src, des).perform()
# action.click_and_hold(src).move_to_element(des).release(des).perform()


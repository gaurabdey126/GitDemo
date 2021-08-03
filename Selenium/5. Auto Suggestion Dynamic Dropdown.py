import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.current_url)

driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(3)     ##### to delay the execution
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a") ### common type CSS n then for loop for validation
print(len(countries))
for country in countries:
    if country.text=='India':
        country.click()
        break
print (driver.find_element_by_id("autosuggest").get_attribute('value'))   ####.get_attribute is used as the text value goes of on Refreshing
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"
driver.close()
#
# The getAttribute() method fetches the text contained by an attribute in an html document.
# If a value is not set for an attribute, null value is returned. The attribute is passed as a parameter to the method.

# # So the getText() method gives the text present between the start and end html tags (which is not hidden by CSS) and
# the getAttribute() method identifies the key value pairs within the html tags.
import pytest
from selenium import webdriver

## This is hook and way of invoking command from command line terminal
# Below is the syntax

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):    #### request is an instance when fixture is used

    browser_name = request.config.getoption("browser_name")   ### this is taking from the command line terminal

    #### BASED ON BROWSER IT WILL SELECT
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\geckodriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(7)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver     ### since "return" will not work as "yield" is there... cls.driver is class driver
                                    ### any class calling this fixture..will have this driver assigned to it...
                                    ### no need to return anything
    yield
    driver.close()



import pytest
from selenium import webdriver

# this fixture is used to do PRE and POST condition of any method
@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    yield
    driver.close()
    print("End of the execution")

# this fixture is used for a data load
@pytest.fixture()
def data_load():
    print("User Profile Data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

# this fixture is used to call multiple data for a single method
@pytest.fixture(params=["Chrome", "Mozilla", "IE"]) ### params= is a must and it should hold the multiple data
def browser(request):                               ### request argument is manadatory
    return request.param                            ### this exact is mandatory

# this fixture is used to call (multiple+multiple) set of data for a single method
@pytest.fixture(params=[("Chrome","Ethan", "Hunt"), ("Mozilla","James"), ("IE","Jason")]) ### params= is a must and it should hold the multiple data
def browser_name(request):                               ### request argument is manadatory
    return request.param
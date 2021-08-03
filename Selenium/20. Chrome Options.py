from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-xss-auditor")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("user-agent={userAgent}")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="C:\\Users\gaura\Desktop\Selenium with PYTHON\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
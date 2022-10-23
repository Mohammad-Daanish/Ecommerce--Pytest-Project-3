import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# """Successfully Declared and initialized run time variable and KeyValue (--browser_name) should be matched
#  in CMDB Terminal """


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/Users/saniy/PycharmProjects/pythonProjectPytestFramework/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/saniy/PycharmProjects/pythonProjectPytestFramework/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("C:/Users/saniy/PycharmProjects/pythonProjectPytestFramework/IEDriverServer.exe")
        driver = webdriver.Firefox(service=service_obj)
    # driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    # driver.close()

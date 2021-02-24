from selenium import webdriver
import pytest


# pytest fixture to initialize driver object before each test and close after completion of the test
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="./drivers/chromedriver_win32/chromedriver.exe")
        yield driver
        driver.quit()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="./drivers/geckodriver-v0.29.0-win64/geckodriver.exe")
        yield driver
        driver.quit()


# To get the browser value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# This fixture will return the browser value to the setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Pytest HTML Report
# Hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Just Eat Assessment'
    config._metadata['Module Name'] = 'Search Restaurants'
    config._metadata['Tester'] = 'Abhishek Choudhary'


# Hook to delete/modify Environment info in HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

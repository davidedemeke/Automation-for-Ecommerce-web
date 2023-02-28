import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.....")  # run terminal to specific browser  pytest -v -s test_cases/test_login.py --browser Chrome

    elif browser == 'FireFox':
        driver = webdriver.Firefox()
        print("Launching Chrome Firefox....")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def teardown(cls):
#     # close the browser
#     cls.driver.quit()


#   pytest  HTML report
# hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['module Name'] = 'Customers'
    config._metadata['Tester'] = 'David'


# hook for delete/modify environment info to html report
@pytest.mark.optionalhook()
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)

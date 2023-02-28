import pytest
from selenium import webdriver

from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_001_login:
    BASE_URL = ReadConfig.get_application_url()
    # BASE_URL = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("******Test_001_login*******")
        self.logger.info("******Verify HP title****")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error('****** Page title test faild *****')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(username=self.USERNAME)
        self.lp.set_password(password=self.PASSWORD)
        self.lp.submit_login()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_login.png")
            self.driver.close()
            assert False

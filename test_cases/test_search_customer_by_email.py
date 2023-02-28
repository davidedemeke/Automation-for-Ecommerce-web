import string
import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.add_customer_page import AddCustomer
from page_objects.login_page import LoginPage
from page_objects.search_customer_page import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_004_Search_Customer_By_Email:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()

    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("******Test_004_Search_Customer_By_Email*******")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.USERNAME)
        self.lp.set_password(self.PASSWORD)
        self.lp.submit_login()
        self.logger.info('***   Login successfully   ****')

        self.logger.info('***  Starting test_search_customer_by_email test  ****')

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        self.add_cust.click_on_customer_sub_menu()

        self.logger.info("**** searching customer by email_id    **** ")
        search_customer = SearchCustomer(self.driver)
        search_customer.set_email("victoria_victoria@nopCommerce.com")
        search_customer.click_search_btn()
        time.sleep(5)
        status = search_customer.search_customer_by_email("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("TC :Test_004_Search_Customer_By_Email -> test_search_customer_by_email finished")
        self.driver.close()
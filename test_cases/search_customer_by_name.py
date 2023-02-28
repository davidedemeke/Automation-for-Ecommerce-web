import string
import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.add_customer_page import AddCustomer
from page_objects.login_page import LoginPage
from page_objects.search_customer_page import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_005_Search_Customer_By_NAME:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("******Test_005_Search_Customer_By_name******")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.USERNAME)
        self.lp.set_password(self.PASSWORD)
        self.lp.submit_login()
        self.logger.info('***   Login successfully   ****')

        self.logger.info('***  Starting test_search_customer_by_name test  ****')

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        self.add_cust.click_on_customer_sub_menu()

        self.logger.info("**** searching customer by name    **** ")
        search_customer = SearchCustomer(self.driver)
        search_customer.set_first_name("Victoria")
        search_customer.set_last_name("Terces")
        search_customer.click_search_btn()
        time.sleep(5)
        status = search_customer.search_customer_by_name("Victoria Terces ")
        assert True == status
        self.logger.info("TC :Test_005_Search_Customer_By_name -> test_search_customer_by_name finished")
        self.driver.close()

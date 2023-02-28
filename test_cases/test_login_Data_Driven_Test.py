import time

import pytest
from selenium import webdriver

from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import xl_util


class Test_002_DDT_login:
    BASE_URL = ReadConfig.get_application_url()
    path = ".//test_data/loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        """Get data from Excel file and compare it to browser data """
        self.logger.info(" ******* Test_002_DDT_login ******** ")
        self.logger.info(" ******* Verify Login DDT test ******** ")
        self.driver = setup
        self.driver.get(self.BASE_URL)

        self.lp = LoginPage(self.driver)

        self.rows = xl_util.get_row_count(self.path, 'Sheet1')
        print("number of rows ", self.rows)
        list_of_status = []

        for row in range(2, self.rows + 1):
            """ extract data (count,row and data from  test_data/loginData excel file """
            self.user = xl_util.read_data(self.path, 'Sheet1', row, 1)
            self.password = xl_util.read_data(self.path, 'Sheet1', row, 2)
            self.exp = xl_util.read_data(self.path, 'Sheet1', row, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.submit_login()
            time.sleep(5)

            actual_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if actual_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info(" test is passed ")
                    self.lp.click_logout()
                    list_of_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info(" test is fail ")
                    self.lp.click_logout()
                    list_of_status.append("Fail")
            elif actual_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info(" test is failed ")
                    list_of_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info(" test is passed ")
                    list_of_status.append("Pass")

        if 'Fail' not in list_of_status:
            self.logger.info("Login DDT test passed successfully ")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed ")
            self.driver.close()
            assert False

        self.logger.info("End of Login DDT test ")
        self.logger.info("*****completed TC_Test_002_DDT_login**** ")

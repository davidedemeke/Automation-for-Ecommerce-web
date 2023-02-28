import string

from selenium.webdriver.common.by import By

from page_objects.add_customer_page import AddCustomer
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
import random


class Test_003_AddCustomer:
    BASE_URL = ReadConfig.get_application_url()
    USERNAME = ReadConfig.get_user_email()
    PASSWORD = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_add_customer(self, setup):
        self.logger.info("******Test_003_Add_Customer*******")
        self.driver = setup
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.USERNAME)
        self.lp.set_password(self.PASSWORD)
        self.lp.submit_login()
        self.logger.info('***   Login successfully   ****')
        self.logger.info('***  Starting add new customer test  ****')

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        self.add_cust.click_on_customer_sub_menu()

        self.add_cust.click_on_add_new_customer()

        self.logger.info("****  providing customer info   **** ")

        self.email = random_generator() + '@gmail.com'
        self.add_cust.set_email(self.email)
        self.add_cust.set_password('test123')
        self.add_cust.set_customer_rules('Guests')
        self.add_cust.set_manager_of_vendor('Vendor 2')
        self.add_cust.set_gender('Male')
        self.add_cust.set_first_name("David")
        self.add_cust.set_last_name("test")
        self.add_cust.set_dob("01/01/2000")
        self.add_cust.set_company_name("QA ")
        self.add_cust.set_admin_content("This is for testing")
        self.add_cust.click_on_save()

        self.logger.info("****  saving customer info   **** ")

        self.logger.info("****  add customer validation started   **** ")
        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("****  add customer test passed   **** ")
        else:
            self.driver.save_screenshot(".//screenshots//" + "test_add_customer_src.png")
            assert True == False
        self.driver.close()
        self.logger.info("****  ending Add customer test test   **** ")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    # Generate a string of 10 random characters
    return ''.join(random.choice(chars) for x in range(size))

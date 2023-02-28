import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # add customer page
    LNK_CUSTOMER_MAIN_MENU = '//a[@href="#"]//p[contains(text(),"Customers")]'
    LNK_CUSTOMERS_SUB_MENU = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p'
    ADD_NEW_CUSTOMER_BTN = '//a[@class="btn btn-primary"]'
    TEXT_EMAIL = '//input[@id="Email"]'
    TEXT_PASSWORD = '//input[@id="Password"]'
    TXT_FIRST_NAME = '//input[@id="FirstName"]'
    TXT_LAST_NAME = '//input[@id="LastName"]'
    RD_MALE_GENDER = '//input[@id="Gender_Male"]'
    RD_FEMALE_GENDER = '//input[@id="Gender_Female"]'
    TXT_DOB = '//input[@id="DateOfBirth"]'
    TXT_COMPANY_NAME = '//input[@id="Company"]'
    TEXT_CUSTOMER_RULES = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    LST_ITEM_ADMINISTRATORS = '//li[contains(text(),"Administrators")]'
    LST_ITEM_FORUM_MODERATOR = '//li[contains(text(),"Forum Moderators")]'
    LST_ITEM_GUESTS = '//li[contains(text(),"Guest")]'
    LST_ITEM_REGISTERED = '//li[contains(text(),"Registered")]'
    LST_ITEM_VENDORS = '//li[contains(text(),"Vendors")]'
    DRP_MGR_OF_VENDORS = '//*[@id="VendorId"]'
    TXT_ADMIN_CONTENT = '//textarea[@id="AdminComment"]'
    SAVE_BTN = '//button[@name="save"]'

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.LNK_CUSTOMER_MAIN_MENU).click()

    def click_on_customer_sub_menu(self):
        self.driver.find_element(By.XPATH, self.LNK_CUSTOMERS_SUB_MENU).click()

    def click_on_add_new_customer(self):
        self.driver.find_element(By.XPATH, self.ADD_NEW_CUSTOMER_BTN).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.TEXT_EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.TEXT_PASSWORD).send_keys(password)

    def set_customer_rules(self, rule):
        self.driver.find_element(By.XPATH, self.TEXT_CUSTOMER_RULES).click()
        time.sleep(3)
        if rule == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_REGISTERED)
        elif rule == 'Administrators':
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_ADMINISTRATORS)
        elif rule == 'Forum Moderators':
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_FORUM_MODERATOR)
        elif rule == 'Guests':
            # Here user can be Registered or guest user
            time.sleep(3)
            # Remove "register button from the 'Customer rules ' field
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            # set the new "guest" button to 'Customer rules ' field
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_GUESTS)
        elif rule == 'Vendors':
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_VENDORS)
        else:
            self.list_item = self.driver.find_element(By.XPATH, self.LST_ITEM_GUESTS)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def set_manager_of_vendor(self, value):
        """select value from drop down"""
        drop_down = Select(self.driver.find_element(By.XPATH, self.DRP_MGR_OF_VENDORS))
        drop_down.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.RD_MALE_GENDER).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.RD_FEMALE_GENDER).click()
        else:
            self.driver.find_element(By.XPATH, self.RD_MALE_GENDER).click()

    def set_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.TXT_FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.TXT_LAST_NAME).send_keys(last_name)

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.TXT_DOB).send_keys(dob)

    def set_company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.TXT_COMPANY_NAME).send_keys(company_name)

    def set_admin_content(self, admin_content):
        self.driver.find_element(By.XPATH, self.TXT_ADMIN_CONTENT).send_keys(admin_content)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.SAVE_BTN).click()

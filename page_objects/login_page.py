# from selenium import webdriver

from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    textbox_username_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//input[@class="password"]'
    login_btn_xpath = "//button[@class='button-1 login-button']"
    logout_btn_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_btn_link_text).click()

#
# class LoginPage:
#     textbox_username_xpath = '//input[@class="email valid"]'
#     textbox_password_xpath = '//input[@class="password"]'
#     login_btn_xpath = "//button[@class='button-1 login-button']"
#     logout_btn_link_text = 'Logout'
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def set_username(self, username):
#         self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
#         self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)
#
#     def set_password(self, password):
#         self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
#         self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element_by_xpath(self.login_btn_xpath).click()
#
#     def click_logout(self):
#         self.driver.find_element_by_link_text(self.logout_btn_link_text).click()

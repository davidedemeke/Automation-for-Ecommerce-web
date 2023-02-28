from selenium.webdriver.common.by import By


class SearchCustomer:
    TXT_EMAIL = '//*[@id="SearchEmail"]'
    TXT_FIRST_NAME = '//*[@id="SearchFirstName"]'
    TXT_LAST_NAME = '///*[@id="SearchLastName"]'
    SEARCH_BTN = '//*[@id="search-customers"]'

    SEARCH_RESULTS = '//div[@class="dataTables_scrollBody"]'  ###
    TABLE = '//*[@id="customers-grid"]'
    TABLE_ROW = '//*[@id="customers-grid"]//tbody/tr'
    TABLE_COLUMN = '//*[@id="customers-grid"]//tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_elemnt(By.XPATH, self.TXT_EMAIL).clear()
        self.driver.find_elemnt(By.XPATH, self.TXT_EMAIL).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_elemnt(By.XPATH, self.TXT_FIRST_NAME).clear()
        self.driver.find_elemnt(By.XPATH, self.TXT_FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_elemnt(By.XPATH, self.TXT_LAST_NAME).clear()
        self.driver.find_elemnt(By.XPATH, self.TXT_LAST_NAME).send_keys(last_name)

    def click_search_btn(self):
        self.driver.find_elemnt(By.XPATH, self.SEARCH_BTN).click()

    def get_num_of_rows(self):
        return len(self.driver.find_elemnt(By.XPATH, self.TABLE_ROW))

    def get_num_of_column(self):
        return len(self.driver.find_elemnt(By.XPATH, self.TABLE_COLUMN))

    def search_customer_by_email(self, email):
        flag = False
        for row in range(1, self.get_num_of_rows() + 1):
            table = self.driver.find_elemnt(By.XPATH, self.TABLE)
            email_id = table.find_elemnt(By.XPATH, '//table[@id="customers-grid"]/tbody/tr[' + str(row) + ']/td[2]').text
            if email_id == email:
                flag = True
                break
            return flag

    def search_customer_by_name(self, name):
        flag = False
        for row in range(1, self.get_num_of_rows() + 1):
            table = self.driver.find_elemnt(By.XPATH, self.TABLE)
            name_id = table.find_elemnt(By.XPATH, '//table[@id="customers-grid"]/tbody/tr[' + str(row) + ']/td[3]').text
            if name_id == name:
                flag = True
                break
            return flag

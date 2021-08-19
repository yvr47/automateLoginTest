
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Page_login():
    def __init__(self, driver):
        self.driver = driver
        self.usr_link = (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/div[1]/input")
        self.pass_link = (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/div[2]/input")
        self.cmd_link = (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/button")

    def login(self, usr, password):
        print(usr)
        # print(self.driver)
        # self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5) \
            .until(EC.element_to_be_clickable((self.usr_link))) \
            .click()

        WebDriverWait(self.driver, 5) \
            .until(EC.element_to_be_clickable((self.usr_link))) \
            .clear()

        WebDriverWait(self.driver, 5) \
            .until(EC.element_to_be_clickable((self.usr_link))) \
            .send_keys(usr)

        # self.driver.find_element_by_id("ember1636").send_keys(usr)

        self.driver.find_element(*self.pass_link).send_keys(password)
        self.driver.find_element(*self.cmd_link).click()



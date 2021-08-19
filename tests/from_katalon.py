# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')
        # options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-extensions')
        # options.add_argument('--headless')
        options.add_argument('--incongnito')
        # options.add_argument('--disable-infobars')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(executable_path=r'C:\temp\python_selenium_drivers\chromedriver.exe', options = options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://us2.app.sysdig.com/")
        driver.find_element_by_link_text("Sign up for a free trial!").click()
        self.driver.implicitly_wait(10)
        driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept").click()
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[2]/div[2]/div/main/div[3]/div/div/div[2]/div/div/p[2]/a'.replace(
                                                   ' ', '.')))) \
            .click()


        driver.find_element_by_name("FirstName").click()
        driver.find_element_by_name("FirstName").clear()
        driver.find_element_by_name("FirstName").send_keys("Yaumara")

        driver.find_element_by_name("LastName").clear()
        driver.find_element_by_name("LastName").send_keys(u"Valdés")

        Select(driver.find_element_by_name("Country")).select_by_visible_text("Spain")
        driver.find_element_by_name("Email").click()
        driver.find_element_by_name("Email").clear()
        driver.find_element_by_name("Email").send_keys("yaumara@yahoo.com")

        driver.find_element_by_name("Company").clear()
        driver.find_element_by_name("Company").send_keys("None")

        driver.find_element_by_name("Trial_Type__c").click()
        Select(driver.find_element_by_name("Trial_Type__c")).select_by_visible_text(
            "Sysdig Platform (Monitor + Secure)")
        WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div/main/div[2]/div/div/div[2]/form/div[26]/span/button[2]/span[2]'.replace(
                                                   ' ', '.')))) \
            .click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

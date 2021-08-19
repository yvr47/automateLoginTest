# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from page_objects.pageindex import *
from page_objects.pageRegister import *
from page_objects.pageLogin import *
from webdriver_manager.chrome import ChromeDriverManager

class PrincipalTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--start-maximized')
        # options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_registration_link(self):
        driver = self.driver
        print(self.driver)
        driver.get("app.sysdigcloud.com")
        page_index = Page_index(self.driver)
        registration_link = page_index.search_registration_link()
        self.assertEqual(registration_link.text,"Sign up for a free trial!")
        page_index.go_registration_link(registration_link)
        self.driver.implicitly_wait(5)
        page_register = Page_register(self.driver)
        page_register.register()

    def test_login(self):
        driver = self.driver
        driver.get("app.sysdigcloud.com")
        # print(self.driver.title)
        page_login = Page_login(self.driver)
        page_login.login("fd@yahoo.com", "----")
        time.sleep(5)
        self.assertEqual(self.driver.title,"Get Started - Sysdig Monitor")

    # def test_awrongLoginPassword(self):
    #     driver = self.driver
    #     driver.get("app.sysdigcloud.com")
    #     print(self.driver)
    #     page_login = Page_login(self.driver)
    #     page_login.login("fd@yahoo.com", "hh")
    #     time.sleep(5)
    #     self.assertEqual(self.driver.title,"Sysdig Monitor")

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


if __name__ == "__main__":
    unittest.main()


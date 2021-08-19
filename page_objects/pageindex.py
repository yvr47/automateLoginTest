from selenium.webdriver.common.by import By

class Page_index():
    def __init__(self, driver):
        self.driver = driver
        self.search_link = (By.LINK_TEXT, 'Sign up for a free trial!')

    def search_registration_link(self):
        self.driver.implicitly_wait(2)
        registration_link = self.driver.find_element(*self.search_link)
        return registration_link

    def go_registration_link(self, element):
        self.driver.implicitly_wait(5)
        element.click()

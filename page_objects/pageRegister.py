from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Page_register():
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept").click()

        WebDriverWait(self.driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[2]/div[2]/div/main/div[3]/div/div/div[2]/div/div/p[2]/a'.replace(
                                                   ' ', '.')))) \
            .click()

        self.driver.find_element_by_name("FirstName").click()
        self.driver.find_element_by_name("FirstName").clear()
        self.driver.find_element_by_name("FirstName").send_keys("Yaumara")

        self.driver.find_element_by_name("LastName").clear()
        self.driver.find_element_by_name("LastName").clear()
        self.driver.find_element_by_name("LastName").send_keys(u"Valdés")

        Select(self.driver.find_element_by_name("Country")).select_by_visible_text("Spain")
        self.driver.find_element_by_name("Email").click()
        self.driver.find_element_by_name("Email").clear()
        self.driver.find_element_by_name("Email").send_keys("yaumara@yahoo.com")

        self.driver.find_element_by_name("Company").clear()
        self.driver.find_element_by_name("Company").send_keys("None")

        self.driver.find_element_by_name("Trial_Type__c").click()
        Select(self.driver.find_element_by_name("Trial_Type__c")).select_by_visible_text(
            "Sysdig Platform (Monitor + Secure)")
        return WebDriverWait(self.driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div/main/div[2]/div/div/div[2]/form/div[26]/span/button[2]/span[2]'.replace(
                                                   ' ', '.')))) \
            .click()



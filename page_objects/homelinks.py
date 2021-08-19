import unittest
from selenium.common.exceptions import  NoSuchElementException
from connect import set_up
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class HomeLinks(unittest.TestCase):
     def setUp(self):

         con = set_up.Connect()
         self.driver = con.setUp()

     def test_home_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Home"), "Element is not found")
         self.home = self.driver.find_element_by_link_text("Home")
         self._event_test(self.home, By.LINK_TEXT, "Home")


     def test_flight_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Flights"), "Element is not found")
         self.home = self.driver.find_element_by_link_text("Flights")
         self._event_test(self.home, By.LINK_TEXT, "Flights")

     def test_destinations_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Destinations"), "Element is not found")
         self.destinations = self.driver.find_element_by_link_text("Destinations")
         self._event_test(self.home, By.LINK_TEXT, "Destinations")

     def test_contact_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "CONTACT"), "Element is not found")
         self.contact = self.driver.find_element_by_link_text("CONTACT")
         self._event_test(self.home, By.LINK_TEXT, "CONTACT")

     def test_signOn_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "SIGN-ON"), "Element is not found")
         self.sign_on = self.driver.find_element_by_link_text("SIGN-ON")
         self._event_test(self.home, By.LINK_TEXT, "SIGN-ON")

     def test_register_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "REGISTER"), "Element is not found")
         self.register = self.driver.find_element_by_link_text("REGISTER")
         self._event_test(self.home, By.LINK_TEXT, "REGISTER")

     def test_support_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "SUPPORT"), "Element is not found")
         self.support = self.driver.find_element_by_link_text("SUPPORT")
         self._event_test(self.home, By.LINK_TEXT, "SUPPORT")

     def test_hotels_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Hotels"), "Element is not found")
         self.hotels = self.driver.find_element_by_link_text("Hotels")
         self._event_test(self.home, By.LINK_TEXT, "Hotels")

     def test_carRentals_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Car Rentals"), "Element is not found")
         self.car_rentals = self.driver.find_element_by_link_text("Car Rentals")
         self._event_test(self.home, By.LINK_TEXT, "Car Rentals")

     def test_cruises_link(self):
         self.assertTrue(self.is_element_present(By.LINK_TEXT, "Cruises"), "Element is not found")
         self.cruises = self.driver.find_element_by_link_text("Cruises")
         self._event_test(self.home, By.LINK_TEXT, "Cruises")

     def is_element_present(self, how, what):

         '''

         :param how: By Locator Type
         :param what: Locator value
         :return: Exception(if it is not found), otherwise, return True
         '''

         try:
             self.driver.find_element(how, what)

         except NoSuchElementException:
             return False
         return True

     def _event_test(self, element, how, what):
         WebDriverWait(self.driver, 5)\
         .until(expected_conditions.element_to_be_clickable((how, what)))
         element.click()
         self.driver.back()
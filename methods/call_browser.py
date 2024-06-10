import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from methods.short_methods import BrowserAutomation
class LoginTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(self):
        self.obj = BrowserAutomation("chrome")
        self.obj.start_browser()
        self.obj.open_website("https://www.baltech.in/")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


object = LoginTest()
object.setUpClass()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from webdriver_manager.firefox import GeckoDriverManager
import pytest

from Hypeddit.logintest import Logintest
from Hypeddit.loudlink import Loudlinks

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_login(self):

        self.driver.get("https://dev2.hypeddit.com/devlock")

        self.login = Logintest(self.driver)
        self.login.devlock("BetterDevTest8675!")
        self.login.login("harry@baltech.in", "123456")
        time.sleep(2)

        self.loud = Loudlinks(self.driver)
        self.loud.Create_loudlink("https://www.resso.com/in/")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

print("Task completed")
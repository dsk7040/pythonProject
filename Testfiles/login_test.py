from selenium import webdriver
import time
import unittest
from Hypeddit.logintest import Logintest

class LoginTest(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        driver.get("https://dev2.hypeddit.com/devlock")

        login = Logintest(driver)
        login.devlock("BetterDevTest8675!")
        login.login("harry@baltech.in", "123456")
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

print("Login Successful")
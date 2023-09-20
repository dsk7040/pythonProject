from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
import time
import unittest
from Hypeddit.logintest import Logintest
from Hypeddit.smartlink import Smartlink
class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        s = Service("C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login(self):

        self.driver.get("https://dev2.hypeddit.com/devlock")

        self.login = Logintest(self.driver)
        self.login.devlock("BetterDevTest8675!")
        self.login.login("harry@baltech.in", "123456")
        time.sleep(2)

        self.smartlink = Smartlink(self.driver)
        self.smartlink.create_smartlink("https://music.apple.com/in/album/humdard/1111741333?i=1111741446")
    print("Smart Link Created")
    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

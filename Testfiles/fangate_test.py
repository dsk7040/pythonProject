from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
import time
import unittest
from Hypeddit.logintest import Logintest
from Hypeddit.fangate import Fangate
import pytest
from Hypeddit.loudlink import Loudlinks
from Hypeddit.smartlink import Smartlink

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        s = Service("C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.login = Logintest(cls.driver)
        cls.fangate = Fangate(cls.driver)


    def test_01_login(self):

        self.driver.get("https://dev2.hypeddit.com/devlock")
        self.login.devlock("BetterDevTest8675!")
        self.login.login("harry@baltech.in", "123456")
        time.sleep(2)

    def test_02_fangate(self):
        self.fangate.create_fangate("https://open.spotify.com/track/390f3txdKIeV7cCv0thgOB?si=97559592778c4fb7",
                                    "C:\\Users\\Baltech\\Downloads\\Salasar Balaji Tone.mp3", "Arjit singh",
                                    "https://music.apple.com/in/album/humdard/1111741333?i=1111741446")

        time.sleep(2)

        # self.loud = Loudlinks(self.driver)
        # self.loud.Create_loudlink("https://www.resso.com/in/")
        # time.sleep(2)
        # print("LoudLink Success")
        #
        # self.smartlink = Smartlink(self.driver)
        # self.smartlink.create_smartlink("https://music.apple.com/in/album/humdard/1111741333?i=1111741446")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

